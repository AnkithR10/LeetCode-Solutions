import collections
import heapq

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0
            
        # 1. Multi-source BFS to calculate distance to the nearest thief
        dist = [[float('inf')] * n for _ in range(n)]
        queue = collections.deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        
        # 2. Max-Priority Queue to find the path with maximum safeness factor
        # We store (-safeness, r, c) to simulate a Max-Heap using Python's Min-Heap
        pq = [(-dist[0][0], 0, 0)]
        safeness = [[-1] * n for _ in range(n)]
        safeness[0][0] = dist[0][0]
        
        while pq:
            d, r, c = heapq.heappop(pq)
            d = -d
            
            if r == n - 1 and c == n - 1:
                return d
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    # The safeness of a path to (nr, nc) is the minimum of
                    # the current path's safeness and the dist at (nr, nc)
                    new_d = min(d, dist[nr][nc])
                    if new_d > safeness[nr][nc]:
                        safeness[nr][nc] = new_d
                        heapq.heappush(pq, (-new_d, nr, nc))
        
        return 0