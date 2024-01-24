class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        max_counter = 0

        for c in s:
            if c == "(":
                counter += 1
                max_counter = max(max_counter, counter)
            elif c == ")":
                counter -= 1

            

        return max_counter


        