from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours):
        accumulator = 0
        lookup = defaultdict(int)
        for hour in hours:
            current_value = hour % 24
            complement_value = (24 - current_value) % 24
            accumulator += lookup[complement_value]
            lookup[current_value] += 1
        return accumulator