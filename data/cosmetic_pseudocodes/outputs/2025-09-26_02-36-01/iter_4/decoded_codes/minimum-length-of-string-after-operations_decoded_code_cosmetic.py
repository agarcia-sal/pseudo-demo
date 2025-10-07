from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        frequencyMap = Counter(s)
        oddCount = 0
        evenCount = 0
        values = list(frequencyMap.values())
        index = 0
        while index < len(values):
            currentValue = values[index]
            if currentValue % 2 != 0:
                oddCount += 1
            elif currentValue % 2 == 0 and currentValue != 0:
                evenCount += 2
            index += 1
        totalLength = oddCount + evenCount
        return totalLength