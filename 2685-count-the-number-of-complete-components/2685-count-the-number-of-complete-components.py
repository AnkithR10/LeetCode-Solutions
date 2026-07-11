class Solution:
    def countCompleteComponents(self, n, edges):
        # 1. Create adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components = 0
        
        # 2. Iterate through all nodes
        for i in range(n):
            if not visited[i]:
                component_nodes = []
                # 3. Use DFS to find the whole component
                stack = [i]
                visited[i] = True
                while stack:
                    u = stack.pop()
                    component_nodes.append(u)
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
                
                # 4. Check if complete
                m = len(component_nodes)
                e = 0
                for node in component_nodes:
                    e += len(adj[node])
                
                # Each edge is counted twice in undirected graph
                if e == m * (m - 1): 
                    complete_components += 1
                    
        return complete_components