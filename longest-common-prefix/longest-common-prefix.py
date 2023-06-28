class Solution(object):
    def longestCommonPrefix(self, strs):

        cp = ""

        if strs is None or len(strs) == 0 or any(len(word) == 0 for word in strs):
            return cp

        sw = min((word for word in strs if word), key=len)
        strs.remove(sw)

        for i in range(len(sw)):
            for j in range(len(strs)):
                if sw[i] != strs[j][i]:
                    return cp
            cp += sw[i]
        return cp
    