class Solution(object):
    def minimumPushes(self, word):
        count = [0] * 26

        for ch in word:
            count[ord(ch) - ord('a')] += 1

        count.sort(reverse=True)

        ans = 0

        for i in range(26):
            ans += count[i] * (i // 8 + 1)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna