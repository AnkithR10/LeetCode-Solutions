class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        valid_islands_count = 0
        
        def dfs(r, c):
            # Out of bounds or water (0) or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
                
            # Capture current cell value and mark as visited by setting to 0
            current_val = grid[r][c]
            grid[r][c] = 0
            
            # Explore all 4 directions and accumulate the island sum
            total_sum = current_val
            total_sum += dfs(r + 1, c)
            total_sum += dfs(r - 1, c)
            total_sum += dfs(r, c + 1)
            total_sum += dfs(r, c - 1)
            
            return total_sum

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    # Find total value of the current island via DFS
                    island_sum = dfs(i, j)
                    
                    # Check if total value is divisible by k
                    if island_sum % k == 0:
                        valid_islands_count += 1
                        
        return valid_islands_count