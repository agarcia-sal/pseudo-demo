from collections import defaultdict
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        accumulator = 0
        count_map = defaultdict(int)
        index = 0
        n = len(hours)

        while index < n:
            current_hour = hours[index]
            mod_val = current_hour % 24

            needed_val = 24 - mod_val
            if needed_val >= 24:
                needed_val -= 24

            accumulator += count_map[needed_val]
            count_map[mod_val] += 1

            index += 1

        return accumulator