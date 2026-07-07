class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        # We only need the last two values to calculate the next
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
            
        return b