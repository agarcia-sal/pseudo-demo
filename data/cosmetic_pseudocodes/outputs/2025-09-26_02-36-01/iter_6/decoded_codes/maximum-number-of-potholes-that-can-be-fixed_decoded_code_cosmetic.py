class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        def splitString(input_str: str, delimiter: str) -> list[str]:
            resultList = []
            currentIndex = 0
            delimiterIndex = indexOf(input_str, delimiter, currentIndex)
            while delimiterIndex != -1:
                resultList.append(input_str[currentIndex:delimiterIndex])
                currentIndex = delimiterIndex + 1
                delimiterIndex = indexOf(input_str, delimiter, currentIndex)
            resultList.append(input_str[currentIndex:len(input_str)])
            return resultList

        def indexOf(text: str, char: str, startAt: int) -> int:
            for i in range(startAt, len(text)):
                if characterAt(text, i) == char:
                    return i
            return -1

        def characterAt(text: str, pos: int) -> str:
            return text[pos]

        def sortByLengthAscending(arr: list[str]) -> list[str]:
            def comparator(a: str, b: str) -> bool:
                return len(a) < len(b)
            sortedArr = arr[:]
            n = len(sortedArr)
            for i in range(n - 1):
                for j in range(n - i - 1):
                    if not comparator(sortedArr[j], sortedArr[j + 1]):
                        sortedArr[j], sortedArr[j + 1] = sortedArr[j + 1], sortedArr[j]
            return sortedArr

        def processSegmentList(segmentList: list[str], currentBudget: int, fixedSum: int, idx: int) -> int:
            if idx >= len(segmentList):
                return fixedSum
            segmentString = segmentList[idx]
            segmentLength = len(segmentString)

            if segmentLength == 0:
                return processSegmentList(segmentList, currentBudget, fixedSum, idx + 1)

            fixCost = segmentLength + 1  # segmentLength + (1*1)
            if fixCost <= currentBudget:
                newFixedSum = fixedSum + segmentLength
                newBudget = currentBudget - fixCost
                return processSegmentList(segmentList, newBudget, newFixedSum, idx + 1)
            else:
                return handlePartialFix(segmentLength, currentBudget, fixedSum, segmentList, idx)

        def handlePartialFix(n: int, currBudget: int, fixedCount: int, segList: list[str], index: int) -> int:
            if n <= 0 or currBudget <= 0:
                return processSegmentList(segList, currBudget, fixedCount, index + 1)
            currentCost = n + 1
            if currBudget >= currentCost:
                return processSegmentList(segList, currBudget - currentCost, fixedCount + n, index + 1)
            else:
                return handlePartialFix(n - 1, currBudget, fixedCount, segList, index)

        segments = splitString(road, '.')
        sortedSegments = sortByLengthAscending(segments)
        totalFixed = processSegmentList(sortedSegments, budget, 0, 0)
        return totalFixed