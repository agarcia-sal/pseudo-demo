from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours):
        frequency_map = defaultdict(int)
        total_pairs = 0

        def processIndex(idx):
            nonlocal total_pairs
            if idx >= len(hours):
                return
            current_value = hours[idx]
            mod_val = current_value % 24
            complement_val = (24 - mod_val) % 24
            total_pairs += frequency_map[complement_val]
            frequency_map[mod_val] += 1
            processIndex(idx + 1)

        processIndex(0)
        return total_pairs