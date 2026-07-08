class Solution(object):
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        memo = {}
        
        # Self-contained GCD helper
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def solve(idx, g1, g2):
            if idx == len(nums):
                return 1 if (g1 == g2 and g1 > 0) else 0
            
            state = (idx, g1, g2)
            if state in memo:
                return memo[state]
            
            # Choice 1: Skip
            res = solve(idx + 1, g1, g2)
            
            # Choice 2: Add to first subsequence
            new_g1 = nums[idx] if g1 == 0 else get_gcd(g1, nums[idx])
            res = (res + solve(idx + 1, new_g1, g2)) % MOD
            
            # Choice 3: Add to second subsequence
            new_g2 = nums[idx] if g2 == 0 else get_gcd(g2, nums[idx])
            res = (res + solve(idx + 1, g1, new_g2)) % MOD
            
            memo[state] = res
            return res
            
        return solve(0, 0, 0)