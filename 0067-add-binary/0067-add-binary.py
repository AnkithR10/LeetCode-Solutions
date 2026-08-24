class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        
        # Loop until both strings are fully traversed and no carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            # Add bit from string 'a' if available
            if i >= 0:
                total += int(a[i])
                i -= 1
                
            # Add bit from string 'b' if available
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # The current bit is total % 2 (either 0 or 1)
            result.append(str(total % 2))
            
            # The new carry is total // 2 (either 0 or 1)
            carry = total // 2
            
        # Since we collected digits from right to left, reverse the result list and join
        return "".join(reversed(result))