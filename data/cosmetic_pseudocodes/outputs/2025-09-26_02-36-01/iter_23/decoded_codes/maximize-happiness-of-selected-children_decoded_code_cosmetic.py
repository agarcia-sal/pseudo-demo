from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        def swap(arr: List[int], posA: int, posB: int) -> None:
            arr[posA], arr[posB] = arr[posB], arr[posA]

        def partition(arr: List[int], left: int, right: int) -> int:
            pivotVal = arr[right]
            fillPos = left - 1
            for iterator in range(left, right):
                if arr[iterator] >= pivotVal:
                    fillPos += 1
                    swap(arr, fillPos, iterator)
            swap(arr, fillPos + 1, right)
            return fillPos + 1

        def quicksortDescending(arr: List[int], left: int, right: int) -> None:
            if left < right:
                pivotIndex = partition(arr, left, right)
                quicksortDescending(arr, left, pivotIndex - 1)
                quicksortDescending(arr, pivotIndex + 1, right)

        quicksortDescending(happiness, 0, len(happiness) - 1)

        accumulatedScore = 0
        decrementCounter = 0
        indexPointer = 0
        while indexPointer <= k - 1:
            tempNumber = happiness[indexPointer] - decrementCounter
            if tempNumber < 0:
                tempNumber = 0
            accumulatedScore += tempNumber
            decrementCounter += 1
            indexPointer += 1

        return accumulatedScore