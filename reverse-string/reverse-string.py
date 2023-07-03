class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        mid = len(s) // 2
        end = len(s) - 1

        for i in range(mid):
            if s[i] != s[end]:
                s[i], s[end] = s[end], s[i]
            end -= 1
            