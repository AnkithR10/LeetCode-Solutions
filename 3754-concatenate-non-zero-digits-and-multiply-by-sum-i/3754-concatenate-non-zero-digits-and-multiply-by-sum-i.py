class Solution(object):
    def sumAndMultiply(self, n):
        
        # Convert n to string to iterate over digits
        s = str(n)
        
        # Collect non-zero digits
        non_zero_digits = [int(digit) for digit in s if digit != '0']
        
        # If there are no non-zero digits, x = 0
        if not non_zero_digits:
            return 0
        
        # Form the integer x by joining the digits
        x = int("".join(map(str, non_zero_digits)))
        
        # Calculate the sum of digits in x
        digit_sum = sum(non_zero_digits)
        
        # Return the product
        return x * digit_sum