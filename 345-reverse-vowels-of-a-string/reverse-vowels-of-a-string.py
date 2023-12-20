class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        string = list(s)
        start, end = 0, len(string)-1

        while start < end:
            
            while start < end and string[start] not in VOWELS:
                start += 1
                
            while start < end and string[end] not in VOWELS:
                end -= 1
                
            string[start], string[end] = string[end], s[start]
            start += 1
            end -= 1
               
        return ''.join(string)
        