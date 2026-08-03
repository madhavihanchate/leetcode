class Solution(object):
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            curr = 0
            dp[i] = float("-inf")

            for j in range(i, min(i + 3, n)):
                curr += stoneValue[j]
                dp[i] = max(dp[i], curr - dp[j + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna