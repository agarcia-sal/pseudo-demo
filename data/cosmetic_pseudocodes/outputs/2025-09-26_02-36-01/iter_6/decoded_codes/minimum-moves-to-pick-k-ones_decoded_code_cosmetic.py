class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        def isOne(value: int) -> bool:
            return value == 1

        positionsToOnes = []
        idx = 0
        limit = len(nums)
        while idx < limit:
            if isOne(nums[idx]):
                positionsToOnes.append(idx)
            idx += 1

        if len(positionsToOnes) == 0:
            return 2 * k

        countOnes = len(positionsToOnes)
        partialSums = [0] * (countOnes + 1)

        pos = 0
        while pos < countOnes:
            partialSums[pos + 1] = partialSums[pos] + positionsToOnes[pos]
            pos += 1

        def cost(start: int, end: int) -> int:
            centerIndex = (start + end) // 2
            medianVal = positionsToOnes[centerIndex]
            accumulatedCost = 0

            iterator = start
            upperBound = centerIndex - 1
            while iterator <= upperBound:
                diff = medianVal - positionsToOnes[iterator]
                indexDiff = centerIndex - iterator
                accumulatedCost += diff - indexDiff
                iterator += 1

            iterator = centerIndex + 1
            endIndex = end
            while iterator <= endIndex:
                diff = positionsToOnes[iterator] - medianVal
                indexDiff = iterator - centerIndex
                accumulatedCost += diff - indexDiff
                iterator += 1

            return accumulatedCost

        movesMinimum = 2_147_483_647
        startIndex = 0
        upperLimit = countOnes - k
        while startIndex <= upperLimit:
            endIndex = startIndex + k - 1
            segmentCost = cost(startIndex, endIndex)

            if k % 2 == 1:
                middle = (startIndex + endIndex) // 2
                medianSingle = positionsToOnes[middle]
                neededChanges = endIndex - middle - (medianSingle - positionsToOnes[middle] - 1)
            else:
                leftMiddle = (startIndex + endIndex) // 2
                rightMiddle = leftMiddle + 1
                medianLeft = positionsToOnes[leftMiddle]
                medianRight = positionsToOnes[rightMiddle]
                distance = rightMiddle - leftMiddle - 1
                medianGap = medianRight - medianLeft - 1
                neededChanges = distance - medianGap

            if neededChanges > maxChanges:
                segmentCost += neededChanges - maxChanges

            if segmentCost < movesMinimum:
                movesMinimum = segmentCost

            startIndex += 1

        return movesMinimum