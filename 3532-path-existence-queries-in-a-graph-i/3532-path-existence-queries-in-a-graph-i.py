class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # component_id[i] will store the ID of the connected component for node i
        component_id = [0] * n
        curr_id = 0
        
        for i in range(n - 1):
            if nums[i+1] - nums[i] > maxDiff:
                curr_id += 1
            component_id[i+1] = curr_id
            
        # For each query [u, v], they are connected if they share the same component ID
        answer = []
        for u, v in queries:
            answer.append(component_id[u] == component_id[v])
            
        return answer