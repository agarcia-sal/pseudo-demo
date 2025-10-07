from typing import List, Tuple

class Fenwick:
    def __init__(self, n: int):
        # Initialize Fenwick tree with n+1 zeroes (1-based indexing)
        self.tree = [0] * (n + 1)

    def add(self, i: int) -> None:
        v = 1
        n = len(self.tree)
        while i < n:
            self.tree[i] += v
            i += i & (-i)

    def pre(self, i: int) -> int:
        result = 0
        while i > 0:
            result += self.tree[i]
            i &= i - 1
        return result

    def query(self, l: int, r: int) -> int:
        # sum in range [l, r]
        return self.pre(r) - self.pre(l - 1)


class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        zippedPairs = [(xCoord[i], yCoord[i]) for i in range(len(xCoord))]
        zippedPairs.sort(key=lambda p: (p[0], p[1]))

        # Unique sorted ys maintaining original order before sort then sort ascending
        seenYs = set()
        uniqueYsSet = []
        for val in yCoord:
            if val not in seenYs:
                seenYs.add(val)
                uniqueYsSet.append(val)
        uniqueYsSet.sort()

        ans = -1

        fenw = Fenwick(len(uniqueYsSet))

        def binarySearchLeft(arr: List[int], target: int) -> int:
            leftIndex = 0
            rightIndex = len(arr)
            while leftIndex < rightIndex:
                pivot = leftIndex + (rightIndex - leftIndex) // 2
                if arr[pivot] < target:
                    leftIndex = pivot + 1
                else:
                    rightIndex = pivot
            return leftIndex

        firstY = zippedPairs[0][1]
        firstIndex = binarySearchLeft(uniqueYsSet, firstY) + 1
        fenw.add(firstIndex)

        previousMap = {}

        def pairwise(lst: List[Tuple[int, int]]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
            output = []
            i = 0
            limit = len(lst) - 1
            while i < limit:
                output.append((lst[i], lst[i + 1]))
                i += 1
            return output

        pairList = pairwise(zippedPairs)

        for leftPair, rightPair in pairList:
            x1, y1 = leftPair
            x2, y2 = rightPair
            yPos = binarySearchLeft(uniqueYsSet, y2) + 1
            fenw.add(yPos)
            if x1 != x2:
                continue
            ql = binarySearchLeft(uniqueYsSet, y1) + 1
            currentVal = fenw.query(ql, yPos)
            if y2 in previousMap:
                pn = previousMap[y2]
                if pn[1] == y1 and (pn[2] + 2) == currentVal:
                    wDiff = x2 - pn[0]
                    hDiff = y2 - y1
                    candidate = wDiff * hDiff
                    if candidate > ans:
                        ans = candidate
            previousMap[y2] = (x1, y1, currentVal)

        return ans