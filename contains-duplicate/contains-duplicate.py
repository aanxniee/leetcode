from collections import Counter

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        c = Counter(nums)
        m = max(c, key=c.get)

        if c[m] == 1:
            return False
        else:
            return True