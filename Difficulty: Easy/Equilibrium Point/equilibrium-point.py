class Solution:
    def findEquilibrium(self, arr):
        total= sum(arr)
        ls = 0
        for i in range(len(arr)):
            rs = total - ls - arr[i]
            if ls == rs:
                return i
            else:
                ls += arr[i]
        return -1 
