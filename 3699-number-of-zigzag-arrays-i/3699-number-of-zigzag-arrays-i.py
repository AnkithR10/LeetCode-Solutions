class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = r - l + 1
        
        # dp[dir][x] where dir is 0 (down) or 1 (up), and x is the value offset from l
        # Base case for length 1: every single value is a valid start
        # dir = 0 means we can go down next (so previous step went up, or we just started)
        # To handle length 1 and 2 properly, let's build up iteratively.
        
        # Let's use dp tables of size m for values from l to r
        # dp_down[x]: number of valid sequences ending at value x (where the last step was down, meaning next must be up)
        # dp_up[x]: number of valid sequences ending at value x (where the last step was up, meaning next must be down)
        
        MOD = 10**9 + 7
        m = r - l + 1
        
        # For length 1, each value can start a sequence
        # We can represent states: 
        # 0: last step was down (so next must be up, meaning y > x)
        # 1: last step was up (so next must be down, meaning y < x)
        # Wait, a single element has no previous step yet. Any element can be the start.
        
        dp_down = [1] * m  # ways to end at x such that next must be down (y < x) -> wait, if next is down, previous step must have been up? 
        # Let's align with hint 1 & 2:
        # dp[i][dir][x]: count of length-i sequences ending at value x where dir is the required next comparison (0 = down, 1 = up).
        # If dir = 0 (next must be down), we sum previous dp[1][x] for x > y.
        # If dir = 1 (next must be up), we sum previous dp[0][x] for x < y.
        
        # Base case: length 1. For length 1, any start has no restriction on next move yet, 
        # or we can think of building from length 2.
        # Let's initialize for length 1: every value x can be the start. 
        # If we place x, we can either choose to go up next or go down next.
        # Actually, let's look at length 2: any pair (x, y) with x != y is valid.
        
        # Let's initialize arrays for the current length:
        # up[x]: number of valid arrays ending at x where the last step was UP (so next must be DOWN, y < x)
        # down[x]: number of valid arrays ending at x where the last step was DOWN (so next must be UP, y > x)
        
        up = [1] * m     # length 1 ending at x, last step could be considered anything, but let's build up from length 2.
        down = [1] * m
        
        # Length 2: all pairs (x, y) with x != y
        # If x < y, last step was UP (ending at y).
        # If x > y, last step was DOWN (ending at y).
        
        current_up = [0] * m
        current_down = [0] * m
        
        # For length 2:
        # prefix sums of previous 'down' for y > x -> for up[y], we sum down[x] for x < y
        # prefix sums of previous 'up' for y < x -> for down[y], we sum up[x] for x > y
        
        # Let's initialize for length 2 directly:
        # up[y] = sum(down[x] for x < y)
        # down[y] = sum(up[x] for x > y)
        
        # Initial length 1 counts before taking steps:
        # Each single element can be viewed as having 1 way.
        
        u = [1] * m  # ways ending at x with last step UP
        d = [1] * m  # ways ending at x with last step DOWN
        
        for _ in range(n - 1):
            next_u = [0] * m
            next_d = [0] * m
            
            # For next_u[y], we need sum of d[x] for x < y
            # Compute prefix sums of d
            pref_d = 0
            for y in range(m):
                next_u[y] = pref_d
                pref_d = (pref_d + d[y]) % MOD
                
            # For next_d[y], we need sum of u[x] for x > y
            # Compute suffix sums of u
            suff_u = 0
            for y in range(m - 1, -1, -1):
                next_d[y] = suff_u
                suff_u = (suff_u + u[y]) % MOD
                
            u = next_u
            d = next_d
            
        return (sum(u) + sum(d)) % MOD