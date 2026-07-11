class Solution:
    def alternatingXOR(self, nums, target1, target2):
        MOD = 10**9 + 7
        n = len(nums)
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] ^ nums[i]
            
        dp1 = [0] * (n + 1)
        dp2 = [0] * (n + 1)
        
        mp1 = {0: 1}
        mp2 = {}
        
        for i in range(1, n + 1):
            curr_pref = pref[i]
            
            needed1 = curr_pref ^ target1
            dp1[i] = mp1.get(needed1, 0)
            
            needed2 = curr_pref ^ target2
            dp2[i] = mp2.get(needed2, 0)
            
            mp1[curr_pref] = (mp1.get(curr_pref, 0) + dp2[i]) % MOD
            mp2[curr_pref] = (mp2.get(curr_pref, 0) + dp1[i]) % MOD
            
        return (dp1[n] + dp2[n]) % MOD