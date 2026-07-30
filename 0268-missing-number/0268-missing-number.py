class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        s = ( n * ( n+ 1) ) // 2
        totalsum = sum(nums)
        return (s - totalsum)