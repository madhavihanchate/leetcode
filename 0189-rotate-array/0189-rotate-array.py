class Solution(object):
    def rotate(self, nums, k):
        # Length of the array
        n = len(nums)
        # If k is greater than n
        k = k % n
        # Reverse the entire array
        nums.reverse()  # 7654321
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k]) #5674321
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:]) #5671234