from math import inf

class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        onesIndices = []
        iterator = 0
        while iterator < len(nums):
            if nums[iterator] == 1:
                onesIndices.append(iterator)
            iterator += 1

        if len(onesIndices) == 0:
            return k * 2

        totalOnes = len(onesIndices)
        prefix = [0] * (totalOnes + 1)
        idx = 0
        while idx < totalOnes:
            prefix[idx + 1] = prefix[idx] + onesIndices[idx]
            idx += 1

        def cost(start: int, finish: int) -> int:
            midpoint = (start + finish) // 2
            medianValue = onesIndices[midpoint]
            accruedCost = 0

            leftPos = start
            while leftPos < midpoint:
                accruedCost += (medianValue - onesIndices[leftPos]) - (midpoint - leftPos)
                leftPos += 1

            rightPos = midpoint + 1
            while rightPos <= finish:
                accruedCost += (onesIndices[rightPos] - medianValue) - (rightPos - midpoint)
                rightPos += 1

            return accruedCost

        minimumMoves = inf
        startPos = 0
        while startPos <= totalOnes - k:
            endPos = startPos + k - 1
            segmentCost = cost(startPos, endPos)

            if k % 2 == 1:
                midIndex = (startPos + endPos) // 2
                medianVal = onesIndices[midIndex]
                requiredChanges = endPos - midIndex - (medianVal - onesIndices[midIndex] - 1)
            else:
                leftMid = (startPos + endPos) // 2
                rightMid = leftMid + 1
                leftMedian = onesIndices[leftMid]
                rightMedian = onesIndices[rightMid]
                requiredChanges = rightMid - leftMid - 1 - (rightMedian - leftMedian - 1)

            if requiredChanges > maxChanges:
                segmentCost += requiredChanges - maxChanges

            if segmentCost < minimumMoves:
                minimumMoves = segmentCost

            startPos += 1

        return minimumMoves