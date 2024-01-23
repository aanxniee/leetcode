import collections

class Solution:
    """
    graph traversal, airpoint = vertex, flight = edge
    directed graph
    eulerian path visits every edge exactly once -- exactly this problem, just with a fixed starting point, JFK

    hierholzer's algorithm: choose any starting vertex v, and follow a trail of edges from that vertex until returning to v. this creates the first circle in the graph. if the circle covers all nodes, it is an eulerian cycle. if not, choose another node with unvisited edges, repeat to create another circle (subtour). connect all circles to create a eulerian cycle

    eulerian path: from a starting vertex, follow unused edges until you get stuck at a vertex with no more unvisited outgoing edges. backtrack to the nearest neighbor vertex in the current path that has unused edges and repeat the process until all edges have been used. the first vertex we got stuck at is the ENDPOINT of our eulerian path

    from JFK, follow the outgoing and unused edges until we get stuck at some vertex. follow this vertex back to reconstruct the path
    """

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # create a graph for each airport and map it to a list of airports it goes to
        # ie. { "JFK" : ["SFO", "ATL"] }
        # using defaultdict to provide default value (list) for non existent keys
        graph = collections.defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)
        
        # sort the destination airports in descending order lexically oto pop last element instead of first which is expensive
        # we want to go to smaller lexically first
        for src in graph.keys():
            graph[src].sort(reverse=True)

        stk, res = ["JFK"], []
      
        # starting from JFK, keep adding the next available airport (following the path). if we reach an airport where we cant go further --> len(graph[airport] is 0, add to result (this airport is done)
        while stk:
            airport = stk[-1]

            if airport in graph and len(graph[airport]):
                stk.append(graph[airport].pop())
            else:
                res.append(stk.pop())
        
        # returning reverse because we add the last airport first --> first airport JFK
        return res[::-1]