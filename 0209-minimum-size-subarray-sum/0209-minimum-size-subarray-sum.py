class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)

        minlen = float('inf')
        left = 0
        curr_sum = 0

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum >= target:
                minlen = min(minlen, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if minlen == float('inf') else minlen

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna