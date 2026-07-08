class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)
        
        # 1. Identify non-zero digits and their positions
        nonzero_indices = [i for i, char in enumerate(s) if char != '0']
        nonzero_vals = [int(s[i]) for i in nonzero_indices]
        
        # 2. Precompute for queries
        # Prefix sum of digits
        prefix_sum = [0] * (len(nonzero_vals) + 1)
        for i in range(len(nonzero_vals)):
            prefix_sum[i+1] = (prefix_sum[i] + nonzero_vals[i])
            
        # Prefix for the concatenated number
        # P[i] = (d_0 * 10^(i-1) + ... + d_{i-1} * 10^0) % MOD
        # To get substring [i, j], we use: (P[j+1] - P[i] * 10^(len)) % MOD
        powers = [1] * (len(nonzero_vals) + 1)
        prefix_val = [0] * (len(nonzero_vals) + 1)
        for i in range(len(nonzero_vals)):
            powers[i+1] = (powers[i] * 10) % MOD
            prefix_val[i+1] = (prefix_val[i] * 10 + nonzero_vals[i]) % MOD
            
        import bisect
        
        ans = []
        for l, r in queries:
            # Map original range to compressed index range
            start = bisect.bisect_left(nonzero_indices, l)
            end = bisect.bisect_right(nonzero_indices, r)
            
            if start >= end:
                ans.append(0)
                continue
            
            # Sum of digits
            digit_sum = prefix_sum[end] - prefix_sum[start]
            
            # Concatenated number x
            length = end - start
            x = (prefix_val[end] - prefix_val[start] * powers[length]) % MOD
            
            ans.append((x * digit_sum) % MOD)
            
        return ans