class Solution:
    """
    need to resolve collisions if:
    1. stack is non empty
    2. current asteroid is -ve
    3. prev asteroid (top of stack) is +ve
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:

                # prev asteroid is smaller, remove +ve asteroid and continue with comparison
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue 

                # atseroids are equal, destroy both
                if stack[-1] == -asteroid:
                    stack.pop()

                break # if prev asteroid is bigger, curr asteroid is destroyed (don't need to do anything)
            else:
                # current asteroid destroyed all other asteroids
                stack.append(asteroid)
        return stack