from collections import defaultdict
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        frequencyMap = defaultdict(int)
        totalPairs = 0
        idx = 0
        while idx < len(hours):
            currHour = hours[idx]
            modValue = ((currHour + 24) - 24 * (currHour // 24)) % 24
            neededComp = (24 - modValue) % 24
            totalPairs += frequencyMap[neededComp]
            frequencyMap[modValue] += 1
            idx += 1
        return totalPairs