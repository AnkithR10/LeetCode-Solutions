class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap characters
            s[left], s[right] = s[right], s[left]
            
            # Move pointers towards each other
            left += 1
            right -= 1