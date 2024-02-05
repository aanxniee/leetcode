from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        ans = 0
        left, right = 0, len(nums) - 1

        while left < right:

            if nums[right] + nums[left] == k:
                ans += 1
                left += 1
                right -= 1
            elif nums[right] + nums[left] > k:
                right -= 1
            else:
                left += 1

        return ans
        
        