class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Iterate over all possible values of p and q
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                
                # Check segment 1: 0 to p is strictly increasing
                is_p1 = all(nums[i] < nums[i+1] for i in range(p))
                
                # Check segment 2: p to q is strictly decreasing
                is_p2 = all(nums[i] > nums[i+1] for i in range(p, q))
                
                # Check segment 3: q to n-1 is strictly increasing
                is_p3 = all(nums[i] < nums[i+1] for i in range(q, n - 1))
                
                if is_p1 and is_p2 and is_p3:
                    return True
                    
        return False