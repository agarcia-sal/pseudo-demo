from collections import defaultdict
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        frequency_map = defaultdict(int)
        total_pairs = 0
        for current_hour in hours:
            mod_val = current_hour % 24
            needed_val = (24 - mod_val) % 24
            total_pairs += frequency_map[needed_val]
            frequency_map[mod_val] += 1
        return total_pairs