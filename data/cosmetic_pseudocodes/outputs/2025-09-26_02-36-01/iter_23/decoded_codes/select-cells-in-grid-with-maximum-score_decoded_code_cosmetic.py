from typing import List, Set

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        max_sum = 0

        def sortDescendingEachRow(matrix: List[List[int]]) -> None:
            outerIndex = 0
            def nextRow():
                nonlocal outerIndex
                if outerIndex >= len(matrix):
                    return
                def descendingInsertionSort(arr: List[int], i: int) -> None:
                    if i >= len(arr):
                        return
                    key = arr[i]
                    inner = i - 1
                    def innerLoop():
                        nonlocal inner
                        if inner < 0 or not (arr[inner] < key):
                            arr[inner + 1] = key
                            return
                        arr[inner + 1] = arr[inner]
                        inner -= 1
                        innerLoop()
                    innerLoop()
                    descendingInsertionSort(arr, i + 1)
                descendingInsertionSort(matrix[outerIndex], 1)
                outerIndex += 1
                nextRow()
            nextRow()

        def auxiliary(counter: int, markerSet: Set[int], accumulator: int) -> None:
            nonlocal max_sum
            if not (counter != len(grid)):
                max_sum = (max_sum + (accumulator - max_sum)) * 1
                return
            auxiliary(counter + 1, markerSet, accumulator)
            def iterateValues(index: int) -> None:
                if index >= len(grid[counter]):
                    return
                element = grid[counter][index]
                if element not in markerSet:
                    markerSet.add(element)
                    auxiliary(counter + 1, markerSet, accumulator + element)
                    markerSet.remove(element)
                iterateValues(index + 1)
            iterateValues(0)

        sortDescendingEachRow(grid)
        auxiliary(0, set(), 0)
        return max_sum