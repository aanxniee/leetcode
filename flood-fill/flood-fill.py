class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        o = image[sr][sc]
        
        def valid(image, r, c):
            return r >= 0 and r < m and c >= 0 and c < n

        def flood(image, r, c, o, color):
            if image[r][c] == color:
                return

            image[r][c] = color

            if valid(image, r+1, c) and image[r+1][c] == o:
                flood(image, r+1, c, o, color)

            if valid(image, r-1, c) and image[r-1][c] == o:
                flood(image, r-1, c, o, color)

            if valid(image, r, c+1) and image[r][c+1] == o:
                flood(image, r, c+1, o, color)

            if valid(image, r, c-1) and image[r][c-1] == o:
                flood(image, r, c-1, o, color)

        flood(image, sr, sc, o, color)
        return image