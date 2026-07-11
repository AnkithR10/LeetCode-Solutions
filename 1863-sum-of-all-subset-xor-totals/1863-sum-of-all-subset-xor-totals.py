class Solution:
    def subsetXORSum(self, nums):
        res = 0
        for n in nums:
            res |= n
        return res << (len(nums) - 1)