class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        def lengthOf(s: str) -> int:
            count = 0
            while count < len(s):
                count += 1
            return count

        def splitOnDot(text: str) -> list[str]:
            pieces = []
            current = ""
            idx = 0
            maxIdx = lengthOf(text)
            while idx < maxIdx:
                if text[idx] == '.':
                    pieces.append(current)
                    current = ""
                else:
                    current += text[idx]
                idx += 1
            pieces.append(current)
            return pieces

        def sortByLengthAsc(arr: list[str]) -> list[str]:
            sortedArr = arr[:]
            changed = True
            while changed:
                changed = False
                i = 0
                limit = lengthOf(sortedArr) - 1
                while i < limit:
                    if lengthOf(sortedArr[i]) > lengthOf(sortedArr[i + 1]):
                        sortedArr[i], sortedArr[i + 1] = sortedArr[i + 1], sortedArr[i]
                        changed = True
                    i += 1
            return sortedArr

        segments = splitOnDot(road)
        sortedSegments = sortByLengthAsc(segments)
        totalFixed = 0
        segIndex = 0
        segCount = lengthOf(sortedSegments)
        while segIndex < segCount:
            currentSegment = sortedSegments[segIndex]
            lengthSeg = lengthOf(currentSegment)
            if lengthSeg == 0:
                segIndex += 1
                continue
            neededCost = lengthSeg + 1
            if neededCost <= budget:
                totalFixed += lengthSeg
                budget -= neededCost
            else:
                decN = lengthSeg
                while decN > 0 and budget > 0:
                    testCost = decN + 1
                    if budget >= testCost:
                        totalFixed += decN
                        budget -= testCost
                        break
                    decN -= 1
            segIndex += 1
        return totalFixed