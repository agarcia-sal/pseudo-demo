from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        maxSumVal = 0

        def insert(setCol: dict, item: int) -> None:
            setCol[item] = True

        def remove(setCol: dict, item: int) -> None:
            del setCol[item]

        def contains(setCol: dict, item: int) -> bool:
            return item in setCol

        def sortDescending(arr: List[int]) -> None:
            def quickSort(start: int, end: int) -> None:
                if start >= end:
                    return
                pivotIndex = start
                leftIdx = start + 1
                rightIdx = end
                while leftIdx <= rightIdx:
                    while leftIdx <= end and arr[leftIdx] >= arr[pivotIndex]:
                        leftIdx += 1
                    while rightIdx > start and arr[rightIdx] <= arr[pivotIndex]:
                        rightIdx -= 1
                    if leftIdx < rightIdx:
                        arr[leftIdx], arr[rightIdx] = arr[rightIdx], arr[leftIdx]
                arr[pivotIndex], arr[rightIdx] = arr[rightIdx], arr[pivotIndex]
                quickSort(start, rightIdx - 1)
                quickSort(rightIdx + 1, end)

            quickSort(0, len(arr) - 1)

        for indexVar in range(len(grid)):
            sortDescending(grid[indexVar])

        def helper(rindex: int, takenSet: dict, accSum: int) -> None:
            nonlocal maxSumVal
            if rindex >= len(grid):
                if accSum > maxSumVal:
                    maxSumVal = accSum
                return
            # Case 1: skip current row
            helper(rindex + 1, takenSet, accSum)
            # Case 2: pick each element if not taken yet
            for element in grid[rindex]:
                if not contains(takenSet, element):
                    insert(takenSet, element)
                    helper(rindex + 1, takenSet, accSum + element)
                    remove(takenSet, element)

        helper(0, {}, 0)
        return maxSumVal