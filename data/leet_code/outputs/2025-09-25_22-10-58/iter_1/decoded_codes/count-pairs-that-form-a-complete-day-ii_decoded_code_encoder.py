from collections import defaultdict
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainder_count = defaultdict(int)
        pairs = 0
        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24
            pairs += remainder_count[complement]
            remainder_count[remainder] += 1
        return pairs