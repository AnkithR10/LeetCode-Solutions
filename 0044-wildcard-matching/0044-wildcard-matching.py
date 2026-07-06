class Solution(object):
    def isMatch(self, s, p):
        s_ptr, p_ptr = 0, 0
        last_star = -1
        match_ptr = 0
        
        while s_ptr < len(s):
            # Case 1: Match characters or '?'
            if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
                s_ptr += 1
                p_ptr += 1
            # Case 2: '*' encountered
            elif p_ptr < len(p) and p[p_ptr] == '*':
                last_star = p_ptr
                match_ptr = s_ptr
                p_ptr += 1
            # Case 3: Mismatch, but we saw a '*' earlier
            elif last_star != -1:
                p_ptr = last_star + 1
                match_ptr += 1
                s_ptr = match_ptr
            # Case 4: Mismatch and no '*'
            else:
                return False
        
        # Check if remaining characters in pattern are all '*'
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            
        return p_ptr == len(p)