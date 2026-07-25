class Solution(object):
    def carPooling(self, trips, capacity):
        max_location = max(to for _, _, to in trips)

        diff = [0] * (max_location + 1)

        for trip in trips:
            passengers, start, end = trip
            diff[start] += passengers
            diff[end] -= passengers

        current = 0

        for i in range(len(diff)):
            current += diff[i]

            if current > capacity:
                return False

        return True