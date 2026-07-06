class Solution(object):
    def removeCoveredIntervals(self, intervals):
        # Sort by start point ascending, then by end point descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        max_end = 0
        
        for _, end in intervals:
            # If the current interval's end is beyond the max_end seen so far,
            # it is not covered.
            if end > max_end:
                count += 1
                max_end = end
                
        return count