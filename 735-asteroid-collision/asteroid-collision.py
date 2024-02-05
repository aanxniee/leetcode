class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for asteroid in asteroids:
            while stk and stk[-1] > 0 and asteroid < 0:

                if stk[-1] == -asteroid:
                    stk.pop()
                    break

                elif stk[-1] < -asteroid:
                    stk.pop()
                    continue
                    
                elif stk[-1] > -asteroid:
                    break

            else:
                stk.append(asteroid)

        return stk