from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        def sumValuesRecursively(elements, idx, oddCount, evenCount):
            if idx >= len(elements):
                return oddCount + evenCount
            currentVal = elements[idx]
            isOdd = (currentVal % 2) != 0
            oddNext = oddCount
            evenNext = evenCount
            if isOdd:
                oddNext = oddCount + 1
            else:
                if currentVal != 0:
                    evenNext = evenCount + 2
            return sumValuesRecursively(elements, idx + 1, oddNext, evenNext)

        frequencyMap = Counter(s)
        valueList = list(frequencyMap.values())
        finalResult = sumValuesRecursively(valueList, 0, 0, 0)
        return finalResult