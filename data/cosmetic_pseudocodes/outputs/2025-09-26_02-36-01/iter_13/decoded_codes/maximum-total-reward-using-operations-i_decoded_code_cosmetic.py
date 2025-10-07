from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        def auxiliaryDepthSearch(currentSum: int) -> int:
            def insertPosition(sortedArray: List[int], target: int) -> int:
                def loopSearch(low: int, high: int, pos: int) -> int:
                    if low >= high:
                        return low
                    mid = (low + high) // 2
                    if target <= sortedArray[mid]:
                        return loopSearch(low, mid, pos)
                    else:
                        return loopSearch(mid + 1, high, pos)
                return loopSearch(0, len(sortedArray), 0)

            insertionIndex = insertPosition(rewardValues, currentSum)
            bestReward = 0
            indexCounter = insertionIndex
            length = len(rewardValues)

            while indexCounter < length:
                candidateValue = rewardValues[indexCounter]
                # Check for overflow or no gain condition
                if currentSum + candidateValue > currentSum:
                    recursiveSum = currentSum + candidateValue
                    deeperReward = auxiliaryDepthSearch(recursiveSum)
                    candidateTotal = candidateValue + deeperReward
                    if bestReward < candidateTotal:
                        bestReward = candidateTotal
                indexCounter += 1
            return bestReward

        def partition(arr: List[int], left: int, right: int) -> int:
            pivotVal = arr[right]
            i = left - 1
            for j in range(left, right):
                if arr[j] <= pivotVal:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[right] = arr[right], arr[i + 1]
            return i + 1

        def quickSort(arr: List[int], left: int, right: int) -> None:
            if left < right:
                pivotIndex = partition(arr, left, right)
                quickSort(arr, left, pivotIndex - 1)
                quickSort(arr, pivotIndex + 1, right)

        if rewardValues:
            quickSort(rewardValues, 0, len(rewardValues) - 1)
        return auxiliaryDepthSearch(0)