from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        def comp(a: Point, b: Point) -> bool:
            if a.x < b.x:
                return True
            elif a.x == b.x and a.y > b.y:
                return True
            else:
                return False

        def swap(arr: List[Point], idx1: int, idx2: int) -> None:
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

        def quicksort(arr: List[Point], left: int, right: int) -> None:
            if left >= right:
                return
            pivot = arr[right]
            store_idx = left
            for curr_idx in range(left, right):
                if comp(arr[curr_idx], pivot):
                    swap(arr, curr_idx, store_idx)
                    store_idx += 1
            swap(arr, store_idx, right)
            quicksort(arr, left, store_idx - 1)
            quicksort(arr, store_idx + 1, right)

        if not points:
            return 0

        quicksort(points, 0, len(points) - 1)

        totalPairs = 0
        idx1 = 0
        n = len(points)
        while idx1 < n - 1:
            idx2 = idx1 + 1
            while idx2 < n:
                px1, py1 = points[idx1].x, points[idx1].y
                px2, py2 = points[idx2].x, points[idx2].y

                if not (px1 <= px2 and py1 >= py2):
                    idx2 += 1
                    continue

                isValid = True
                innerIdx = idx1 + 1
                while innerIdx < idx2:
                    pxk, pyk = points[innerIdx].x, points[innerIdx].y
                    if (px1 <= pxk <= px2) and (py2 <= pyk <= py1):
                        isValid = False
                        break
                    innerIdx += 1

                if isValid:
                    totalPairs += 1

                idx2 += 1
            idx1 += 1

        return totalPairs