class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        c = Counter(s1)
        ws = len(s1)
        m = 0
        
        for i in range(len(s2)):
            if s2[i] in c:
                c[s2[i]] -= 1
                if c[s2[i]] == 0:
                    m += 1

            if i >= ws and s2[i-ws] in c:
                if c[s2[i-ws]] == 0:
                    m -= 1
                c[s2[i-ws]] += 1

            if m == len(c):
                return True

        return False