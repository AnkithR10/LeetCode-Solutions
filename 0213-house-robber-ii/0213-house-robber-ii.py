class Solution(object):
    def rob(self, nums):
        """:type nums: List[int]

        :rtype: int
        """
        # Edge case: if there's only one house, rob it.
        if len(nums) == 1:
            return nums[0]

        # Helper function for the standard linear House Robber problem
        def rob_linear(sub_nums):
            prev2, prev1 = 0, 0
            for money in sub_nums:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current
            return prev1

        # The max money is either:
        # 1. Excluding the last house: nums[0] to nums[-2]
        # 2. Excluding the first house: nums[1] to nums[-1]
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))