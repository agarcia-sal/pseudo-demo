from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours):
        freq_map = defaultdict(int)
        total_pairs = 0
        for current_hour in hours:
            rem_val = current_hour % 24  # remainder of hours mod 24
            comp_val = (24 - rem_val) % 24
            total_pairs += freq_map[comp_val]
            freq_map[rem_val] += 1
        return total_pairs