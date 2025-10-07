from typing import List

class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        def sortAscending(array: List[str]) -> None:
            i = 0
            n = len(array)
            while i < n - 1:
                j = i + 1
                while j < n:
                    if len(array[i]) > len(array[j]):
                        array[i], array[j] = array[j], array[i]
                    j += 1
                i += 1

        def splitByPeriod(text: str) -> List[str]:
            result = []
            startIndex = 0
            for idx, ch in enumerate(text):
                if ch == '.':
                    result.append(text[startIndex:idx])
                    startIndex = idx + 1
            result.append(text[startIndex:])
            return result

        def processSegment(index: int, segments: List[str], remainingBudget: int, totalFixed: int) -> int:
            if index >= len(segments):
                return totalFixed

            segment = segments[index]
            lengthOfSegment = len(segment)
            if lengthOfSegment == 0:
                return processSegment(index + 1, segments, remainingBudget, totalFixed)

            requiredCost = lengthOfSegment + 1
            if requiredCost <= remainingBudget:
                updatedFixed = totalFixed + lengthOfSegment
                updatedBudget = remainingBudget - requiredCost
                return processSegment(index + 1, segments, updatedBudget, updatedFixed)

            decrementCount = lengthOfSegment
            while decrementCount > 0 and remainingBudget > 0:
                requiredCost = decrementCount + 1
                if remainingBudget >= requiredCost:
                    updatedFixed = totalFixed + decrementCount
                    updatedBudget = remainingBudget - requiredCost
                    return processSegment(index + 1, segments, updatedBudget, updatedFixed)
                decrementCount -= 1

            return totalFixed

        parts = splitByPeriod(road)
        sortAscending(parts)
        fixedCount = 0
        finalResult = processSegment(0, parts, budget, fixedCount)
        return finalResult