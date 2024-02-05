class Solution:

    """
    1. find the smallest number in the subsequence. make it as small as possible
    2. find the second smallest number in the subsequence. make it as small as possible
       first < n <= second (and then we set second = n)
    3. if n > first and second, we found the third number, return true

    2 1 5 0 4 6

    n = 2, first = 2
    n = 1, first = 1
    n = 5, first = 1 , second = 5
    n = 0, first = 0, second = 5
    n = 4, first = 0, second = 4
    n = 6, first = 0, second = 4, third = 6 (0, 4, 6) --> True
    """
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = float("inf")
        second = float("inf")

        for n in nums:
            if n <= first:
                first = n

            elif n <= second:
                second = n

            else:
                return True

        return False