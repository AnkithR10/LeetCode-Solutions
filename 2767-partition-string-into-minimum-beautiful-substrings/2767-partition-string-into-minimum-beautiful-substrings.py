class Solution:
    def minimumBeautifulSubstrings(self, s):
        # Precompute binary representations of powers of 5
        # 5^0=1, 5^1=5, 5^2=25, 5^3=125, 5^4=625, 5^5=3125, 5^6=15625
        beautiful = {bin(5**i)[2:] for i in range(7)}
        n = len(s)
        memo = {}

        def backtrack(index):
            if index == n:
                return 0
            if index in memo:
                return memo[index]
            
            res = float('inf')
            # Try every possible substring starting from index
            for end in range(index + 1, n + 1):
                sub = s[index:end]
                # Beautiful numbers cannot have leading zeros
                if sub in beautiful:
                    res = min(res, 1 + backtrack(end))
            
            memo[index] = res
            return res

        ans = backtrack(0)
        return ans if ans != float('inf') else -1