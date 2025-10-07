from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours):
        modulo_freqs = defaultdict(int)
        total_pairs = 0
        idx = 0
        while idx < len(hours):
            current_hour = hours[idx]
            mod_val = current_hour - (current_hour // 24) * 24
            needed_complement = (24 - mod_val) % 24
            total_pairs += modulo_freqs[needed_complement]
            modulo_freqs[mod_val] += 1
            idx += 1
        return total_pairs