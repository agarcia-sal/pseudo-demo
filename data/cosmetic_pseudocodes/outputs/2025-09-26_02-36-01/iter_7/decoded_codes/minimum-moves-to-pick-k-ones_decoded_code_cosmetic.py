class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        positionIndices = []
        lenNums = len(nums)
        idx = 0
        while idx < lenNums:
            if nums[idx] == 1:
                positionIndices.append(idx)
            idx += 1

        if len(positionIndices) == 0:
            return k * 2  # k times (1 + 1)

        totalOnes = len(positionIndices)
        accumPrefix = [0] * (totalOnes + 1)
        posCounter = 0
        while posCounter < totalOnes:
            accumPrefix[posCounter + 1] = accumPrefix[posCounter] + positionIndices[posCounter]
            posCounter += 1

        def cost(startIndex: int, endIndex: int) -> int:
            midpoint = (startIndex + endIndex) // 2
            centerVal = positionIndices[midpoint]
            totalCost = 0
            leftWalker = startIndex
            while leftWalker < midpoint:
                totalCost += (centerVal - positionIndices[leftWalker]) - (midpoint - leftWalker)
                leftWalker += 1
            rightWalker = midpoint + 1
            while rightWalker <= endIndex:
                totalCost += (positionIndices[rightWalker] - centerVal) - (rightWalker - midpoint)
                rightWalker += 1
            return totalCost

        minimumMoves = float('inf')
        startIdx = 0
        maxStart = totalOnes - k
        while startIdx <= maxStart:
            finishIdx = startIdx + k - 1
            calculatedCost = cost(startIdx, finishIdx)

            if k % 2 == 1:
                midPos = (startIdx + finishIdx) // 2
                medVal = positionIndices[midPos]
                neededChanges = finishIdx - midPos - (medVal - positionIndices[midPos] - 1)
            else:
                leftMid = (startIdx + finishIdx) // 2
                rightMid = leftMid + 1
                leftMedian = positionIndices[leftMid]
                rightMedian = positionIndices[rightMid]
                neededChanges = rightMid - leftMid - 1 - (rightMedian - leftMedian - 1)

            if neededChanges > maxChanges:
                calculatedCost += (neededChanges - maxChanges)

            if calculatedCost < minimumMoves:
                minimumMoves = calculatedCost

            startIdx += 1

        return minimumMoves