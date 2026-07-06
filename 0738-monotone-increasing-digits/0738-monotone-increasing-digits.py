class Solution(object):
    def monotoneIncreasingDigits(self, n):
        s = list(str(n))
        length = len(s)
        
        # Find the first dip from the left
        # We use a marker 'i' to track where we need to start setting 9s
        i = 1
        while i < length and s[i-1] <= s[i]:
            i += 1
            
        # If the number is already monotone, return it
        if i == length:
            return n
        
        # Backtrack to handle cases like 332 -> 329 -> 299
        while i > 0 and s[i-1] > s[i]:
            s[i-1] = str(int(s[i-1]) - 1)
            i -= 1
            
        # Set all digits after the adjustment index to '9'
        for j in range(i + 1, length):
            s[j] = '9'
            
        return int("".join(s))
        