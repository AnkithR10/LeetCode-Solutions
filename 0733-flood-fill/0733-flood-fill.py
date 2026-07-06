class Solution(object):
    def floodFill(self, image, sr, sc, color):
        originalColor = image[sr][sc]
        
        # If the starting pixel is already the target color, no changes needed
        if originalColor == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            # If out of bounds or the pixel is not the color we want to replace
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != originalColor:
                return
            
            # Update the color
            image[r][c] = color
            
            # Recurse for 4-directionally adjacent pixels
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        dfs(sr, sc)
        return image