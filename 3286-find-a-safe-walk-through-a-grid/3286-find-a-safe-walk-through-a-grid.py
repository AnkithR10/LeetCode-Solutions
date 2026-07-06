class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        # dist stores the minimum cost (number of 1s) to reach cell (r, c)
        dist = [[float('inf')] * n for _ in range(m)]
        
        # Initial cost at (0, 0)
        start_cost = grid[0][0]
        dist[0][0] = start_cost
        
        # Deque for 0-1 BFS
        queue = deque([(0, 0)])
        
        while queue:
            r, c = queue.popleft()
            
            # Explore 4 directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    cost = grid[nr][nc]
                    if dist[r][c] + cost < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + cost
                        # If weight is 0, append to front; if 1, append to back
                        if cost == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
                            
        # We need health - cost >= 1, which means cost <= health - 1
        return dist[m-1][n-1] < health