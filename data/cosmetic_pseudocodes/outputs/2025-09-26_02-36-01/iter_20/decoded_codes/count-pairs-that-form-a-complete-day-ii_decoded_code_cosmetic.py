from collections import defaultdict
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        def modulus24(value: int) -> int:
            acc = value
            while acc >= 24:
                acc -= 24
            while acc < 0:
                acc += 24
            return acc

        storage_map = defaultdict(int)
        total_pairs = 0
        i7jk = 0

        while i7jk < len(hours):
            current_val = hours[i7jk]
            r4xp = modulus24(current_val)
            cmp6 = modulus24(24 - r4xp)
            total_pairs += storage_map.get(cmp6, 0)
            storage_map[r4xp] += 1
            i7jk += 1

        return total_pairs