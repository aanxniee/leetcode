class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l = []
        nums1.sort()
        nums2.sort()

        i = j = 0
        a, b = len(nums1), len(nums2)

        while i < a and j < b:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                l.append(nums1[i])
                i += 1
                j += 1
        
        return l