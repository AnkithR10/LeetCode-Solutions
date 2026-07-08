class Solution(object):
    def findTargetSumWays(self, nums, target):
        total_sum = sum(nums)
        
        # Check if the target is reachable
        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0
        
        subset_target = (target + total_sum) // 2
        
        # dp[i] will store the number of ways to get sum i
        dp = [0] * (subset_target + 1)
        dp[0] = 1
        
        for num in nums:
            # Iterate backwards to ensure each number is used only once
            for i in range(subset_target, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[subset_target]