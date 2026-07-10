class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)
        
        # 1. Skip Whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
            
        # 2. Handle Sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # 3. Read Digits and build result
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1
            
        # Apply sign
        result *= sign
        
        # 4. Handle 32-bit integer bounds
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result