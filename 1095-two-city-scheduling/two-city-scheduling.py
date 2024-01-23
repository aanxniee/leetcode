class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        cost is length 2n
        need n people at each city

        for each person, find the difference between cost b and cost a

        if difference > 0, b is more expensive than a
        else, a is more expensive than b

        the larger (magnitude) the difference, the more expensive it is

        sort by

        """

        costs.sort(key = lambda x : x[1] - x[0])

        cost = 0
        n = len(costs) // 2

        for i in range(n):
           cost += costs[i][1] + costs[i+n][0]
                
        return cost
        