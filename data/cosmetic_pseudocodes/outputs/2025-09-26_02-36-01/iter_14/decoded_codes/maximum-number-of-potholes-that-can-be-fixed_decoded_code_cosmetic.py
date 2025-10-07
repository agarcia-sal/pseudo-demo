class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        def computeLength(s: str) -> int:
            idx = 0
            while idx < len(s):
                idx += 1
            return idx

        def splitByDot(text: str) -> list[str]:
            result = []
            startIdx = 0
            pos = 0
            while pos < len(text):
                if text[pos] == '.':
                    result.append(text[startIdx:pos])
                    startIdx = pos + 1
                pos += 1
            if startIdx <= len(text):
                result.append(text[startIdx:len(text)])
            return result

        def orderAscendingByLength(arr: list[str]) -> list[str]:
            sortedArr = arr[:]
            changed = True
            while changed:
                changed = False
                i = 0
                while i < len(sortedArr) - 1:
                    if computeLength(sortedArr[i]) > computeLength(sortedArr[i + 1]):
                        sortedArr[i], sortedArr[i + 1] = sortedArr[i + 1], sortedArr[i]
                        changed = True
                    i += 1
            return sortedArr

        def canFix(n: int, available: int) -> bool:
            return not (available < n + 1)  # available >= n + 1

        def fixPartial(length_ref: list[int], budget_ref: list[int], fixedCount_ref: list[int]) -> None:
            # length_ref, budget_ref, fixedCount_ref are single-element lists to allow mutation
            while True:
                if length_ref[0] == 0 or budget_ref[0] == 0:
                    break
                currentCost = length_ref[0] + 1
                if budget_ref[0] >= currentCost:
                    fixedCount_ref[0] += length_ref[0]
                    budget_ref[0] -= currentCost
                    break
                length_ref[0] -= 1

        pieces = splitByDot(road)
        orderedPieces = orderAscendingByLength(pieces)
        totalFixed = 0

        idx = 0
        while idx < len(orderedPieces):
            segment = orderedPieces[idx]
            segmentLength = computeLength(segment)
            if segmentLength == 0:
                idx += 1
                continue
            repairCost = segmentLength + 1
            if canFix(segmentLength, budget):
                totalFixed += segmentLength
                budget -= repairCost
            else:
                # Use mutable containers to allow modification inside fixPartial
                length_ref = [segmentLength]
                budget_ref = [budget]
                fixedCount_ref = [totalFixed]
                fixPartial(length_ref, budget_ref, fixedCount_ref)
                totalFixed = fixedCount_ref[0]
                budget = budget_ref[0]
            idx += 1

        return totalFixed