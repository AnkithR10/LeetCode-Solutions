class Solution(object):
    def uniquePaths(self, grid):
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # Precompute target cells
        # jump[i][j][0] = target when entering (i, j) from left (moving right)
        # jump[i][j][1] = target when entering (i, j) from top (moving down)
        
        def get_target(r, c, direction):
            # direction: 0 for right, 1 for down
            curr_r, curr_c = r, c
            curr_dir = direction
            
            while 0 <= curr_r < m and 0 <= curr_c < n and grid[curr_r][curr_c] == 1:
                # If current cell is a mirror, change direction
                # If entering from left (curr_dir 0), reflect down (curr_dir 1)
                # If entering from top (curr_dir 1), reflect right (curr_dir 0)
                curr_dir = 1 - curr_dir
                if curr_dir == 0:
                    curr_c += 1
                else:
                    curr_r += 1
            
            if 0 <= curr_r < m and 0 <= curr_c < n:
                return (curr_r, curr_c)
            return None

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0: continue
                
                # Try move right from (i, j) -> (i, j+1)
                if j + 1 < n:
                    target = get_target(i, j + 1, 0)
                    if target:
                        tr, tc = target
                        dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD
                        
                # Try move down from (i, j) -> (i+1, j)
                if i + 1 < m:
                    target = get_target(i + 1, j, 1)
                    if target:
                        tr, tc = target
                        dp[tr][tc] = (dp[tr][tc] + dp[i][j]) % MOD
                        
        return dp[m-1][n-1]