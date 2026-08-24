class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Traverse backwards from the last digit to the first
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry needed, we are done!
            
            # If the digit is 9, it becomes 0 and the loop carries over to the left
            digits[i] = 0
            
        # If we exit the loop, it means all digits were 9 (e.g., [9, 9] -> [1, 0, 0])
        return [1] + digits