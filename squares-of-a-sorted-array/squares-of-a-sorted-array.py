class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [(x**2) for x in nums]
        arr.sort()

        return arr