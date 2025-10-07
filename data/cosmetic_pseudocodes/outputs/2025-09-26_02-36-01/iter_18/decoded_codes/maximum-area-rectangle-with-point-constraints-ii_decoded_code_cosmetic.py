from typing import List, Tuple, Iterator

class Fenwick:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, zxq: int) -> None:
        qta = zxq
        while qta < len(self.tree):
            self.tree[qta] += 1
            qta += qta & (-qta)

    def pre(self, zmv: int) -> int:
        wbo = 0
        tfl = zmv
        while tfl > 0:
            wbo += self.tree[tfl]
            tfl &= tfl - 1
        return wbo

    def query(self, kin: int, vgr: int) -> int:
        return self.pre(vgr) - self.pre(kin - 1)


class Solution:
    def maxRectangleArea(self, lpa: List[int], sod: List[int]) -> int:
        abc: List[Tuple[int, int]] = [(lpa[i], sod[i]) for i in range(len(lpa))]
        abc.sort(key=lambda x: (x[0], x[1]))

        seen_vals = {}
        for val in sod:
            if val not in seen_vals:
                seen_vals[val] = True
        y_unique = sorted(seen_vals.keys())

        def bisect_left(arr: List[int], key: int) -> int:
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < key:
                    low = mid + 1
                else:
                    high = mid
            return low

        mxr = -1
        fenw = Fenwick(len(y_unique))

        def pairwise(lst: List[Tuple[int, int]]) -> Iterator[Tuple[Tuple[int, int], Tuple[int, int]]]:
            pos = 0
            while pos < len(lst) - 1:
                yield (lst[pos], lst[pos + 1])
                pos += 1

        start_idx = bisect_left(y_unique, abc[0][1]) + 1
        fenw.add(start_idx)

        memo = {}

        for px, py in pairwise(abc):
            (x1, y1) = px
            (x2, y2) = py

            y_idx = bisect_left(y_unique, y2) + 1
            fenw.add(y_idx)

            if x1 != x2:
                continue

            cur_val = fenw.query(bisect_left(y_unique, y1) + 1, y_idx)

            if y2 in memo:
                a, b, c = memo[y2]
                if b == y1 and (c + 2) == cur_val:
                    area_candidate = (x2 - a) * (y2 - y1)
                    if area_candidate > mxr:
                        mxr = area_candidate

            memo[y2] = (x1, y1, cur_val)

        return mxr