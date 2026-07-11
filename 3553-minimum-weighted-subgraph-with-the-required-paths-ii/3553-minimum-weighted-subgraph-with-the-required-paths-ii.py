import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Solution:
    def minimumWeight(self, edges, queries):
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        # Binary lifting table and distance arrays
        depth = [0] * n
        dist = [0] * n
        LOG = 18
        up = [[-1] * LOG for _ in range(n)]
        
        def dfs(u, p, d, w_sum):
            depth[u] = d
            dist[u] = w_sum
            up[u][0] = p
            for v, w in adj[u]:
                if v != p:
                    dfs(v, u, d + 1, w_sum + w)
        
        dfs(0, -1, 0, 0)
        
        for i in range(1, LOG):
            for u in range(n):
                if up[u][i-1] != -1:
                    up[u][i] = up[up[u][i-1]][i-1]
        
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for i in range(LOG - 1, -1, -1):
                if depth[u] - (1 << i) >= depth[v]:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]
            
        def get_dist(u, v):
            return dist[u] + dist[v] - 2 * dist[get_lca(u, v)]
            
        results = []
        for src1, src2, dest in queries:
            # The minimum weight subtree containing a, b, and c is:
            # (dist(a, b) + dist(b, c) + dist(c, a)) // 2
            d12 = get_dist(src1, src2)
            d1d = get_dist(src1, dest)
            d2d = get_dist(src2, dest)
            results.append((d12 + d1d + d2d) // 2)
            
        return results