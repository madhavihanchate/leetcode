class Solution(object):
    def missingInteger(self, nums):
        total = nums[0]

        # Longest sequential prefix
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # O(1) average lookup
        nums_set = set(nums)

        while total in nums_set:
            total += 1

        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna