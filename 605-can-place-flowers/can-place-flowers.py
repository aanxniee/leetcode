class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        c = 0

        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:
                left = (i == 0) or flowerbed[i-1] == 0
                right = (i == len(flowerbed) - 1) or flowerbed[i+1] == 0
                
                if left and right:
                    c += 1
                    flowerbed[i] = 1

        return c >= n





        