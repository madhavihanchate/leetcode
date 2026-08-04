class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        s = s.strip()
        for i in range(len(s)-1 , -1 , -1):
            if s[i] != ' ' :
                count =count +1
            else:
                break
        return count

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna