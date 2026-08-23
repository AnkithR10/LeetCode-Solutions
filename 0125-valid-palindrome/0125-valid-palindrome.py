class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Move left pointer until it hits an alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
                
            # Move right pointer until it hits an alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare lowercase versions of both characters
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True