from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        def compareFirstElement(a: List[int], b: List[int]) -> bool:
            return a[0] < b[0]

        def sortPoints(arr: List[List[int]]) -> None:
            def quicksort(low: int, high: int) -> None:
                if low >= high:
                    return
                pivotIndex = low
                pivotValue = arr[high]
                i = low

                def swap(x: int, y: int) -> None:
                    arr[x], arr[y] = arr[y], arr[x]

                for j in range(low, high):
                    if compareFirstElement(arr[j], pivotValue):
                        swap(i, j)
                        i += 1
                swap(i, high)
                quicksort(low, i - 1)
                quicksort(i + 1, high)

            quicksort(0, len(arr) - 1)

        sortPoints(points)

        counter = 0
        boundary = -1

        def process(index: int, limit: int) -> None:
            nonlocal boundary, counter
            if index >= limit:
                return
            p = points[index]
            if p[0] > boundary:
                boundary = p[0] + w
                counter += 1
            process(index + 1, limit)

        process(0, len(points))
        return counter