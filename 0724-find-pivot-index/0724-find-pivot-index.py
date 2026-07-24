class Solution(object):
    def pivotIndex(self, nums):
        total= sum(nums)
        ls = 0
        for i in range(len(nums)):
            rs = total - ls - nums[i]
            if ls == rs:
                return i
            else:
                ls += nums[i]
        return -1 