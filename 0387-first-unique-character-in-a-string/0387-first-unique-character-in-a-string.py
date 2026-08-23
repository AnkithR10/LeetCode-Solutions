class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Build the frequency map
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Step 2: Find the first character with a count of 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
                
        # If no unique character exists
        return -1