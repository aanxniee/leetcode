class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                cur = ''
                num = ''
                while stack[-1] != '[':
                    cur = stack.pop() + cur
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                newString = int(num) * cur
                stack.append(newString)
        return ''.join(stack)