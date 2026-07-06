class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        res=0

        for i in range(n):
            vis=[False]*256
            
            for j in range(i,n):
                if vis[ord(s[j])-ord('a')]==True:
                    break

                else:
                    res=max(res,j-i+1)
                    vis[ord(s[j])-ord('a')]=True
        return res

