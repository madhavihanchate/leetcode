class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        memo = {}
        def dp(i, M):
            if i >= n:
                return 0
            if i + 2 * M >= n:
                return suffix_sum[i]
            if (i, M) in memo:
                return memo[(i, M)]
            best = 0
            for x in range(1, 2 * M + 1):
                best = max(best, suffix_sum[i] - dp(i + x, max(M, x)))
            memo[(i, M)] = best
            return best
        return dp(0, 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna