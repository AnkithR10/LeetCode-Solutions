class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate current area
            current_height = min(height[left], height[right])
            width = right - left
            current_area = current_height * width
            
            # Update max_water if current_area is larger
            max_water = max(max_water, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water