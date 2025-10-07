from typing import List, Tuple

class Fenwick:
    def __init__(self, n: int):
        def initArray(k: int) -> List[int]:
            return [0 for _ in range(k)]
        self.tree = initArray(n + 1)

    def add(self, i: int) -> None:
        def nextIndex(idx: int) -> int:
            return idx + (idx & (-idx))

        def incrementPosition(arr: List[int], pos: int) -> None:
            arr[pos] += 1

        def loopIncrement(idx: int) -> None:
            if idx >= len(self.tree):
                return
            incrementPosition(self.tree, idx)
            loopIncrement(nextIndex(idx))

        loopIncrement(i)

    def pre(self, i: int) -> int:
        def nextIndex(idx: int) -> int:
            return idx & (idx - 1)

        def sumRec(idx: int, accum: int) -> int:
            if idx <= 0:
                return accum
            return sumRec(nextIndex(idx), accum + self.tree[idx])

        return sumRec(i, 0)

    def query(self, l: int, r: int) -> int:
        return self.pre(r) - self.pre(l - 1)


class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        def zipSort(a: List[int], b: List[int]) -> List[Tuple[int, int]]:
            zippedList = [(a[m], b[m]) for m in range(len(a))]

            def bubbleSortPairs(arr: List[Tuple[int, int]]) -> None:
                n = len(arr)
                for i in range(n - 1):
                    for j in range(n - i - 1):
                        if arr[j][0] > arr[j + 1][0] or (arr[j][0] == arr[j + 1][0] and arr[j][1] > arr[j + 1][1]):
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            bubbleSortPairs(zippedList)
            return zippedList

        def uniqueSorted(arr: List[int]) -> List[int]:
            result = []
            for val in arr:
                if not result or result[-1] != val:
                    result.append(val)
            return result

        def bisectLeft(arr: List[int], target: int) -> int:
            def bisectRec(left: int, right: int) -> int:
                if left >= right:
                    return left
                middle = (left + right) // 2
                if arr[middle] < target:
                    return bisectRec(middle + 1, right)
                else:
                    return bisectRec(left, middle)
            return bisectRec(0, len(arr))

        points = zipSort(xCoord, yCoord)
        ys = uniqueSorted(sorted(yCoord))

        ans = -1

        tree = Fenwick(len(ys))
        tree.add(bisectLeft(ys, points[0][1]) + 1)

        pre = {}

        def processPairs(idx: int) -> None:
            nonlocal ans
            if idx >= len(points) - 1:
                return
            p1 = points[idx]
            p2 = points[idx + 1]
            yVal = bisectLeft(ys, p2[1]) + 1
            tree.add(yVal)

            if p1[0] == p2[0]:
                cur = tree.query(bisectLeft(ys, p1[1]) + 1, yVal)
                if p2[1] in pre and pre[p2[1]][1] == p1[1] and pre[p2[1]][2] + 2 == cur:
                    candidate = (p2[0] - pre[p2[1]][0]) * (p2[1] - p1[1])
                    if candidate > ans:
                        ans = candidate
                pre[p2[1]] = (p1[0], p1[1], cur)
            processPairs(idx + 1)

        processPairs(0)

        return ans