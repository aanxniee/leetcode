class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, j in enumerate(numbers):
            r = target - j
            if r in d:
                return [d[r]+1, i+1]
            d[j] = i
