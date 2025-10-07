from typing import List, Tuple, Iterator


class Fenwick:
    def __init__(self, n: int):
        # 1-based Fenwick tree
        self.tree = [0] * (n + 1)

    def add(self, i: int):
        def _apply_update(idx: int):
            if idx < len(self.tree):
                self.tree[idx] += 1
                _apply_update(idx + (idx & (-idx)))
        _apply_update(i)

    def pre(self, i: int) -> int:
        def _accumulate(idx: int, total: int) -> int:
            if idx > 0:
                return _accumulate(idx & (idx - 1), total + self.tree[idx])
            else:
                return total
        return _accumulate(i, 0)

    def query(self, l: int, r: int) -> int:
        temporaryA = self.pre(r)
        temporaryB = self.pre(l - 1)
        return temporaryA - temporaryB


class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        def _sorted_pairs(xs: List[int], ys: List[int]) -> List[Tuple[int, int]]:
            acc = []
            idx = 0
            while idx < len(xs):
                acc.append((xs[idx], ys[idx]))
                idx += 1
            return sorted(acc)

        def _unique_sorted(values: List[int]) -> List[int]:
            result = []
            for v in sorted(values):
                if len(result) == 0 or result[-1] != v:
                    result.append(v)
            return result

        def _bisect_left(arr: List[int], val: int) -> int:
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < val:
                    low = mid + 1
                else:
                    high = mid
            return low

        points = _sorted_pairs(xCoord, yCoord)
        ys = _unique_sorted(yCoord)
        ans = -1
        tree = Fenwick(len(ys))
        tree.add(_bisect_left(ys, points[0][1]) + 1)

        pre = {}

        def _pairwise(lst: List[Tuple[int, int]]) -> Iterator[Tuple[Tuple[int, int], Tuple[int, int]]]:
            i = 0
            while i < len(lst) - 1:
                yield (lst[i], lst[i + 1])
                i += 1

        for pairA, pairB in _pairwise(points):
            x1, y1 = pairA
            x2, y2 = pairB
            y = _bisect_left(ys, y2) + 1
            tree.add(y)

            if x1 != x2:
                continue

            cur = tree.query(_bisect_left(ys, y1) + 1, y)

            if y2 in pre and pre[y2][1] == y1 and pre[y2][2] + 2 == cur:
                candidate = (x2 - pre[y2][0]) * (y2 - y1)
                if candidate > ans:
                    ans = candidate

            pre[y2] = (x1, y1, cur)

        return ans