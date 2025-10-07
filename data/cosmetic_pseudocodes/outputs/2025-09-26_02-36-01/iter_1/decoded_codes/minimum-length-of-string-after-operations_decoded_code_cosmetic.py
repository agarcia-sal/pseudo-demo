from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        frequencyMap = Counter(s)
        oddCount = 0
        evenSum = 0
        for frequency in frequencyMap.values():
            if frequency % 2 != 0:
                oddCount += 1
            elif frequency != 0:
                evenSum += 2
        return oddCount + evenSum