from typing import List, Tuple

class Solution:
    def maxPathLength(self, coordinates: List[Tuple[int, int]], k: int) -> int:
        pivotX = coordinates[k][0]
        pivotY = coordinates[k][1]

        def helper_filterLeft(coords: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            filtered = []
            idx = 0
            while idx < len(coords):
                currX, currY = coords[idx]
                if (currX < pivotX) and not (currY >= pivotY):
                    filtered.append((currX, currY))
                idx += 1
            return filtered

        def helper_filterRight(coords: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            acc = []
            i = 0
            while True:
                if i >= len(coords):
                    break
                valX, valY = coords[i]
                if valX > pivotX and valY > pivotY:
                    acc.append((valX, valY))
                i += 1
            return acc

        leftSubset = helper_filterLeft(coordinates)
        rightSubset = helper_filterRight(coordinates)

        return 1 + self._lengthOfLIS(leftSubset) + self._lengthOfLIS(rightSubset)

    def _lengthOfLIS(self, coordinates: List[Tuple[int, int]]) -> int:
        def cmpFunc(a: Tuple[int, int], b: Tuple[int, int]) -> int:
            if a[0] == b[0]:
                return b[1] - a[1]
            else:
                return a[0] - b[0]

        def _swap(arr: List[Tuple[int, int]], a: int, b: int) -> None:
            arr[a], arr[b] = arr[b], arr[a]

        def _partition(arr: List[Tuple[int, int]], low: int, high: int) -> int:
            pivot = arr[high]
            i = low - 1
            j = low
            while j < high:
                if cmpFunc(arr[j], pivot) < 0:
                    i += 1
                    _swap(arr, i, j)
                j += 1
            _swap(arr, i + 1, high)
            return i + 1

        def _quickSort(arr: List[Tuple[int, int]], low: int, high: int) -> None:
            if low < high:
                p = _partition(arr, low, high)
                _quickSort(arr, low, p - 1)
                _quickSort(arr, p + 1, high)

        def _customSort(arr: List[Tuple[int, int]]) -> None:
            _quickSort(arr, 0, len(arr) - 1)

        _customSort(coordinates)

        def helper_bisectLeft(arr: List[int], target: int) -> int:
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        tailList: List[int] = []
        idx0 = 0
        while idx0 < len(coordinates):
            _unusedX, currY = coordinates[idx0]
            if not tailList:
                tailList.append(currY)
            else:
                if currY > tailList[-1]:
                    tailList.append(currY)
                else:
                    replacerIdx = helper_bisectLeft(tailList, currY)
                    tailList[replacerIdx] = currY
            idx0 += 1

        return len(tailList)