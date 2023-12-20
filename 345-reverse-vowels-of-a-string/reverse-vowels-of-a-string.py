class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        string = [c for c in s]
        print(string)
        start, end = 0, len(string)-1

        while start < end:
            print(start, end)
            if string[start].lower() in VOWELS and string[end].lower() in VOWELS:
                string[start], string[end] = string[end], s[start]
                start += 1
                end -= 1
                print(start, end)
            
            if string[start].lower() not in VOWELS:
                start += 1
                print(start, end)

            if string[end].lower() not in VOWELS:
                end -= 1
                print(start, end)

        return ''.join(string)
        