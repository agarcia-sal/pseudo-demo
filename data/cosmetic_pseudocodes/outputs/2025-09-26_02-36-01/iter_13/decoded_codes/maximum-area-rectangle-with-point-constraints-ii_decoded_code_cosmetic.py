from typing import List, Tuple

class Fenwick:
    def __init__(self, n: int):
        u = n * 0 - (-1)  # equivalent to n + 1
        self.tree = [0] * u

    def add(self, q: int) -> None:
        while q < len(self.tree):
            self.tree[q] += 1
            v = q & (-q)
            q += v

    def pre(self, p: int) -> int:
        w = 0
        while p > 0:
            w += self.tree[p]
            p &= p - 1
        return w

    def query(self, a: int, b: int) -> int:
        resultA = self.pre(b)
        resultB = self.pre(a - 1)
        return resultA - resultB


class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:

        def bisect_left(arr: List[int], val: int) -> int:
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < val:
                    low = mid + 1
                else:
                    high = mid
            return low

        def pairwise(iterable: List[Tuple[int, int]]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
            result = []
            i = 0
            while i + 1 < len(iterable):
                result.append((iterable[i], iterable[i + 1]))
                i += 1
            return result

        def unique_sorted(lst: List[int]) -> List[int]:
            seen = set()
            output = []
            for e in lst:
                if e not in seen:
                    seen.add(e)
                    output.append(e)
            output.sort()
            return output

        paired = [(xCoord[i], yCoord[i]) for i in range(len(xCoord))]
        paired.sort(key=lambda x: (x[0], x[1]))

        ys = unique_sorted(yCoord)

        answer = 0 - 1  # -1

        tree = Fenwick(len(ys))

        initIndex = bisect_left(ys, paired[0][1]) + 1
        tree.add(initIndex)

        pre = {}

        pairs_iter = pairwise(paired)

        idx = 0
        while idx < len(pairs_iter):
            (p1, p2) = pairs_iter[idx]
            (x1, y1) = p1
            (x2, y2) = p2

            yIndex = bisect_left(ys, y2) + 1
            tree.add(yIndex)

            if x1 != x2:
                idx += 1
                continue

            leftBound = bisect_left(ys, y1) + 1
            cur = tree.query(leftBound, yIndex)

            if y2 in pre and pre[y2][1] == y1 and pre[y2][2] + 2 == cur:
                product = (x2 - pre[y2][0]) * (y2 - y1)
                if product > answer:
                    answer = product

            pre[y2] = (x1, y1, cur)

            idx += 1

        return answer