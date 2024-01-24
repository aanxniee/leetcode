class Solution:
    def decodeString(self, s: str) -> str:

        stk = []
        cur = ""
        k = 0

        for c in s:
            if c == "[":
                stk.append((cur, k))
                cur = ""
                k = 0

            elif c == "]":
                prev_s, prev_k = stk.pop()
                cur = prev_s + prev_k * cur
                
            elif c.isdigit():
                k = k * 10 + int(c)
            
            else:
                cur += c

        return cur

        
        