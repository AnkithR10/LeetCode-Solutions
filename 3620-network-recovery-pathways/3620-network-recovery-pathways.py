import heapq
import collections

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        adj = collections.defaultdict(list)
        costs = set()
        
        # Build graph
        for u, v, cost in edges:
            adj[u].append((v, cost))
            costs.add(cost)
        
        sorted_costs = sorted(list(costs))
        
        # Helper function for binary search
        def check(min_score):
            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]  # (cost, node)
            
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]: continue
                if u == n - 1: return d <= k
                
                for v, cost in adj[u]:
                    if online[v] and cost >= min_score:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                            heapq.heappush(pq, (dist[v], v))
            return dist[n-1] <= k

        # Binary Search
        low, high = 0, len(sorted_costs) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if check(sorted_costs[mid]):
                ans = sorted_costs[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans