class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
            
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev_row = triangle[-1]
            current_row = [1]  # Every row starts with 1
            
            # Calculate the interior elements using the previous row
            for j in range(1, len(prev_row)):
                current_row.append(prev_row[j - 1] + prev_row[j])
                
            current_row.append(1)  # Every row ends with 1
            triangle.append(current_row)
            
        return triangle