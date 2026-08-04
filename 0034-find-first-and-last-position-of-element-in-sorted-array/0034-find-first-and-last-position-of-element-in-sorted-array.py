class Solution(object):
    def searchRange(self, nums, target):

        def bound(target, lower):
            left, right = 0, len(nums)

            while left < right:
                mid = (left + right) // 2

                if nums[mid] > target or (lower and nums[mid] == target):
                    right = mid
                else:
                    left = mid + 1

            return left

        first = bound(target, True)

        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        last = bound(target, False) - 1

        return [first, last]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna