class Solution(object):
    def runningSum(self, nums):
        n = len(nums)
        running = [0] * n
        running[0] = nums[0]
        i=1
        while i <= n-1 :
            running[i] = running[i-1] + nums[i] 
            i+=1
        return running 