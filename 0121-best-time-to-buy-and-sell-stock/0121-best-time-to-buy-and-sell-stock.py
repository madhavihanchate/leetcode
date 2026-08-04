class Solution(object):
    def maxProfit(self, prices):
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price

            profit = price - minPrice

            if profit > maxProfit:
                maxProfit = profit

        return maxProfit

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna