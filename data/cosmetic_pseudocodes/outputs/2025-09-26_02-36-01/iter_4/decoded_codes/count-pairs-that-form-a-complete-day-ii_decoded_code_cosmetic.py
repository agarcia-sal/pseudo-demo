from collections import defaultdict
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainderTracker = defaultdict(int)
        resultCount = 0
        idx = 0
        while idx < len(hours):
            currentHour = hours[idx]
            modValue = currentHour % 24
            neededComplement = (24 - modValue) % 24
            resultCount += remainderTracker[neededComplement]
            remainderTracker[modValue] += 1
            idx += 1
        return resultCount