from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours):
        remainder_map = defaultdict(int)
        total_pairs = 0
        index = 0
        max_index = len(hours)
        while index < max_index:
            current_hour = hours[index]
            mod_val = ((current_hour % 24) + 24) % 24
            needed = ((24 - mod_val) % 24)
            total_pairs += remainder_map[needed]
            remainder_map[mod_val] += 1
            index += 1
        return total_pairs