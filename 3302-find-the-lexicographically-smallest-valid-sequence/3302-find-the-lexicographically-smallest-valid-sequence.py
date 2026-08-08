class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)
        if m > n:
            return []
        match_suffix = [0] * (n + 1)
        j = m
        i = n - 1
        while i >= 0:
            if j > 0 and word1[i] == word2[j - 1]:
                j -= 1
            match_suffix[i] = m - j
            i -= 1
        ans = []
        i = 0
        jj = 0
        used_change = False
        while i < n and jj < m:
            if word1[i] == word2[jj]:
                ans.append(i)
                i += 1
                jj += 1
            elif (not used_change) and match_suffix[i + 1] >= m - jj - 1:
                ans.append(i)
                i += 1
                jj += 1
                used_change = True
            else:
                i += 1
        if jj == m:
            return ans
        return []

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna