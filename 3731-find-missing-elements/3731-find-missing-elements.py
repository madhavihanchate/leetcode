class Solution(object):
    def findMissingElements(self, nums):
        ans = []

        s = set(nums)

        for i in range(min(nums), max(nums) + 1):
            if i not in s:
                ans.append(i)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna