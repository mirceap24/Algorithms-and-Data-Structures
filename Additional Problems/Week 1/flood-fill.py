# https://leetcode.com/problems/flood-fill/description/

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        startingColor = image[sr][sc]
        if startingColor == newColor: 
            return image 
        
        def fill(r, c):
            if not (0 <= r < len(image)) or not (0 <= c < len(image[0])) or image[r][c] != startingColor: 
                return 
            image[r][c] = newColor
            fill(r + 1, c)
            fill (r - 1, c)
            fill(r, c + 1)
            fill(r, c - 1)
        
        fill(sr, sc)

        return image