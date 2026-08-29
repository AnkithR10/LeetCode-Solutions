class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define 32-bit integer bounds
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        # Track the sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before updating rev
            # INT_MAX is 2147483647 (so limit // 10 is 214748364)
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0
                
            rev = rev * 10 + digit
            
        return sign * rev