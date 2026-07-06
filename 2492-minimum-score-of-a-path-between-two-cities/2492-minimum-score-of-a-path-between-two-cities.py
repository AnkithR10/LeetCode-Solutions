class Solution(object):
    def minScore(self, n, roads):
        graph = collections.defaultdict(list)
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
            
        min_score = float('inf')
        visited = set()
        queue = collections.deque([1])
        visited.add(1)
        
        while queue:
            node = queue.popleft()
            for neighbor, dist in graph[node]:
                min_score = min(min_score, dist)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score
        