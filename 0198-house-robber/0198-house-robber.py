class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # rob1: max money robbed up to house i-2
        # rob2: max money robbed up to house i-1
        rob1, rob2 = 0, 0
        
        for n in nums:
            # Current max is either:
            # 1. Skipping this house (keep rob2)
            # 2. Robbing this house (add n to rob1)
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2