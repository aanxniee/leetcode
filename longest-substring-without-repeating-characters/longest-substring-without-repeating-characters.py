class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0

        c = set()
        i = j = 0
        m = 0

        while j < len(s):
            if s[j] not in c:
                c.add(s[j])
                j += 1
                m = max(m, j-i)
            else:
                c.remove(s[i])
                i += 1

        return m

