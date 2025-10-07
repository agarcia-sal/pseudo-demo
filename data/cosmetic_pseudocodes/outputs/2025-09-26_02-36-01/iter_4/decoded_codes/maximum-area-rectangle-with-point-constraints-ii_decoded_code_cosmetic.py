from typing import List

class Fenwick:
    def __init__(self, n: int):
        length = n + 1
        self.tree = [0] * length

    def add(self, index: int):
        idx = index
        while idx < len(self.tree):
            self.tree[idx] += 1
            temp = idx & (-idx)
            idx += temp

    def pre(self, index: int) -> int:
        total = 0
        idx = index
        while idx > 0:
            total += self.tree[idx]
            idx = idx & (idx - 1)
        return total

    def query(self, left: int, right: int) -> int:
        preRight = self.pre(right)
        preLeftMinusOne = self.pre(left - 1)
        return preRight - preLeftMinusOne

class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        zippedPoints = [(xCoord[i], yCoord[i]) for i in range(len(xCoord))]
        zippedPoints.sort(key=lambda p: (p[0], p[1]))

        uniqueYsSet = set()
        for y in yCoord:
            uniqueYsSet.add(y)
        ys = sorted(uniqueYsSet)

        answer = -1

        tree = Fenwick(len(ys))

        # Binary search helper to find lower bound index
        def lower_bound(arr: List[int], target: int) -> int:
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        target = zippedPoints[0][1]
        firstYIndex = lower_bound(ys, target) + 1
        tree.add(firstYIndex)

        pre = dict()

        k = 0
        n_points = len(zippedPoints)
        while k < n_points - 1:
            x1, y1 = zippedPoints[k]
            x2, y2 = zippedPoints[k + 1]

            yPos = lower_bound(ys, y2) + 1
            tree.add(yPos)

            if x1 != x2:
                k += 1
                continue

            queryLeft = lower_bound(ys, y1) + 1
            curr = tree.query(queryLeft, yPos)

            if y2 in pre:
                storedX, storedY1, storedCur = pre[y2]
                if storedY1 == y1 and storedCur + 2 == curr:
                    areaWidth = x2 - storedX
                    areaHeight = y2 - y1
                    candidate = areaWidth * areaHeight
                    if candidate > answer:
                        answer = candidate
            pre[y2] = (x1, y1, curr)
            k += 1

        return answer