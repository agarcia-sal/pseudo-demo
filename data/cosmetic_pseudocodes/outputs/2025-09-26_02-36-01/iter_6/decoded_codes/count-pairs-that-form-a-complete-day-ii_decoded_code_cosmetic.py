from collections import defaultdict
from typing import List

class Solution:
    def countCompleteDayPairs(self, durations: List[int]) -> int:
        def Mod24(value: int) -> int:
            return value - (value // 24) * 24

        complement_map = defaultdict(int)
        total_pairs = 0
        index_counter = 0

        def recursiveCount(list_items: List[int], idx: int, acc: int) -> int:
            if idx == len(list_items):
                return acc
            current_val = list_items[idx]
            mod_val = Mod24(current_val)
            comp_val = Mod24(24 - mod_val)
            new_acc = acc + complement_map[comp_val]
            complement_map[mod_val] += 1
            return recursiveCount(list_items, idx + 1, new_acc)

        total_pairs = recursiveCount(durations, index_counter, total_pairs)
        return total_pairs