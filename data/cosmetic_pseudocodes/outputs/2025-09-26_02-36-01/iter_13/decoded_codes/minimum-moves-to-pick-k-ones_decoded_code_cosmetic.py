class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        onePos = [idx for idx, val in enumerate(nums) if val == 1]
        if len(onePos) == 0:
            return 2 * k

        total_ONES = len(onePos)
        prefixSum = [0] * (total_ONES + 1)
        for i in range(total_ONES):
            prefixSum[i + 1] = prefixSum[i] + onePos[i]

        def computeCost(a: int, b: int) -> int:
            center = (a + b) // 2
            pivot = onePos[center]

            def loopLeft(x: int) -> int:
                if x >= center:
                    return 0
                return (pivot - onePos[x] - center + x) + loopLeft(x + 1)

            def loopRight(y: int) -> int:
                if y <= center:
                    return 0
                return (onePos[y] - pivot - y + center) + loopRight(y - 1)

            return loopLeft(a) + loopRight(b)

        minimumMovesFound = float('inf')

        for start in range(total_ONES - k + 1):
            end = start + k - 1
            totalCost = computeCost(start, end)

            if k % 2 != 0:
                midIndex = (start + end) // 2
                midVal = onePos[midIndex]
                changesRequired = (end - midIndex) - (midVal - onePos[midIndex] - 1)
            else:
                leftMid = (start + end) // 2
                rightMid = leftMid + 1
                leftMedian = onePos[leftMid]
                rightMedian = onePos[rightMid]
                changesRequired = (rightMid - leftMid - 1) - (rightMedian - leftMedian - 1)

            if changesRequired > maxChanges:
                totalCost += changesRequired - maxChanges

            if totalCost < minimumMovesFound:
                minimumMovesFound = totalCost

        return minimumMovesFound