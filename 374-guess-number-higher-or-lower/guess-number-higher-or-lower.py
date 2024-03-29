# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        l, r = 0, n
        mid = (l + r) // 2

        while guess(mid) != 0:
            if guess(mid) == 1:
                l = mid + 1
               
            elif guess(mid) == -1:
                r = mid - 1
                
            mid = (l + r) // 2

        return mid