class Solution(object):
    def pathsWithMaxScore(self, board):
        N = len(board)
        MOD = 10**9 + 7
        
        # dp_sum stores max score, dp_count stores number of paths
        dp_sum = [[-1] * N for _ in range(N)]
        dp_count = [[0] * N for _ in range(N)]
        
        # Base case: start at bottom-right
        dp_sum[N-1][N-1] = 0
        dp_count[N-1][N-1] = 1
        
        # Iterate backwards from bottom-right to top-left
        for r in range(N - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if board[r][c] == 'X' or (r == N - 1 and c == N - 1):
                    continue
                
                # Check possible moves: down, right, diagonal-down-right
                for dr, dc in [(0, 1), (1, 0), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    if nr < N and nc < N and dp_sum[nr][nc] != -1:
                        # Current cell value
                        val = 0 if board[r][c] == 'E' else int(board[r][c])
                        new_sum = dp_sum[nr][nc] + val
                        
                        if new_sum > dp_sum[r][c]:
                            dp_sum[r][c] = new_sum
                            dp_count[r][c] = dp_count[nr][nc]
                        elif new_sum == dp_sum[r][c]:
                            dp_count[r][c] = (dp_count[r][c] + dp_count[nr][nc]) % MOD
                            
        result_sum = max(0, dp_sum[0][0])
        result_count = dp_count[0][0] if dp_sum[0][0] != -1 else 0
        
        return [result_sum, result_count]