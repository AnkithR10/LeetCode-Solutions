class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # We start by looking at the first two steps
        prev2 = cost[0]
        prev1 = cost[1]
        
        # Iterate from the third step to the end
        for i in range(2, len(cost)):
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current
            
        # The answer is the minimum of the last two positions, 
        # as we can reach the top from either.
        return min(prev1, prev2)