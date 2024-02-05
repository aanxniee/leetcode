class Solution:
    """
    you know mid is a peak when nums[mid] > nums[mid+1] and nums[mid-1]
    """
    def findPeakElement(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            # case: descending slope, peak to left
            if nums[mid] > nums[mid + 1]:
                r = mid
            
            # case: ascending slope, peak to right
            else:
                l = mid + 1

        return l
        
        