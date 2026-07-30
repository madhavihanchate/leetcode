k = int(input())
rooms = list(map(int, input().split()))

captain = (sum(set(rooms)) * k - sum(rooms)) // (k - 1)

print(captain)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna