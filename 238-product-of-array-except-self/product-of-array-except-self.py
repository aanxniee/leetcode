class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        r = [1 for _ in range(n)]

        pre = post = 1

        for i in range(n):
            r[i] = pre
            pre *= nums[i]

        for i in range(n-1, -1, -1):
            r[i] *= post
            post *= nums[i]

        return r