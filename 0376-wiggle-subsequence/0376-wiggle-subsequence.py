class Solution(object):
    def wiggleMaxLength(self, nums):
        if not nums:
            return 0
        
        # 'up' and 'down' track the length of the longest 
        # wiggle subsequence ending in a rise or fall.
        up = 1
        down = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                # We found a peak, so we extend the 'down' sequence
                up = down + 1
            elif nums[i] < nums[i-1]:
                # We found a valley, so we extend the 'up' sequence
                down = up + 1
                
        return max(up, down)