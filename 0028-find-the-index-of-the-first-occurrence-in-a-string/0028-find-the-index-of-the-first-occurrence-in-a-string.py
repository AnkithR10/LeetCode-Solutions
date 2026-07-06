class Solution(object):
    def strStr(self, haystack, needle):
        h_len, n_len = len(haystack), len(needle)
        
        # Iterate through the haystack
        for i in range(h_len - n_len + 1):
            # Check if the substring matches the needle
            if haystack[i : i + n_len] == needle:
                return i
                
        return -1