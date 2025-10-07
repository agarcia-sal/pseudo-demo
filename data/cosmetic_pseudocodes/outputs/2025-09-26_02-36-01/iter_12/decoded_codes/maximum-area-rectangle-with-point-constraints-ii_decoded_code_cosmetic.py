from typing import List, Tuple, Optional


class Fenwick:
    def __init__(self, n: int):
        def create_zero_list(size: int) -> List[int]:
            result_list = []
            counter = 0
            while counter < size:
                result_list.append(0)
                counter += 1
            return result_list

        self.tree = create_zero_list(n + 1)

    def add(self, i: int) -> None:
        def bit_update(index: int, limit: int, data: List[int]) -> None:
            if index >= limit:
                return
            data[index] += 1
            bit_update(index + (index & (-index)), limit, data)

        bit_update(i, len(self.tree), self.tree)

    def pre(self, i: int) -> int:
        def bit_prefix(index: int, data: List[int]) -> int:
            if index <= 0:
                return 0
            return data[index] + bit_prefix(index & (index - 1), data)

        return bit_prefix(i, self.tree)

    def query(self, l: int, r: int) -> int:
        # binn_search from pseudocode is unused; omitted here as well
        p1 = self.pre(r)
        p2 = self.pre(l - 1)
        return p1 - p2


class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        def pairwise_iter(lst: List[int]):
            idx = 0
            limit = len(lst)

            def inner(n: int) -> Optional[Tuple[int, int]]:
                if n >= limit - 1:
                    return None
                return (lst[n], lst[n + 1])

            return inner(idx)

        def bisect_left(local_array: List[int], target: int) -> int:
            lhs = 0
            rhs = len(local_array)
            while lhs < rhs:
                median = lhs + (rhs - lhs) // 2
                if local_array[median] < target:
                    lhs = median + 1
                else:
                    rhs = median
            return lhs

        def unique_sort(elems: List[int]) -> List[int]:
            accum = []
            seen = set()
            for val in elems:
                if val not in seen:
                    accum.append(val)
                    seen.add(val)
            accum.sort()
            return accum

        def make_pairs(a_list: List[int], b_list: List[int]) -> List[Tuple[int, int]]:
            pairings = []
            idx = 0
            while idx < len(a_list):
                pairings.append((a_list[idx], b_list[idx]))
                idx += 1
            return pairings

        pts = make_pairs(xCoord, yCoord)
        pts.sort(key=lambda x: (x[0], x[1]))

        sorted_unique_y = unique_sort(yCoord)
        answer = -1

        fenwick_tree = Fenwick(len(sorted_unique_y))
        fenwick_tree.add(bisect_left(sorted_unique_y, pts[0][1]) + 1)

        previous = {}

        def pair_blob(lst: List[int]):
            i = 0

            def next_pair() -> Optional[Tuple[int, int]]:
                nonlocal i
                if i >= len(lst) - 1:
                    return None
                return (lst[i], lst[i + 1])

            return next_pair

        idx = 0
        while idx < len(pts) - 1:
            x1y1, x2y2 = pts[idx], pts[idx + 1]
            x1, y1 = x1y1
            x2, y2 = x2y2

            y_val = bisect_left(sorted_unique_y, y2) + 1
            fenwick_tree.add(y_val)

            if x1 != x2:
                idx += 1
                continue

            left_bound = bisect_left(sorted_unique_y, y1) + 1
            current_sum = fenwick_tree.query(left_bound, y_val)

            if y2 in previous and previous[y2][1] == y1 and previous[y2][2] + 2 == current_sum:
                width = x2 - previous[y2][0]
                height = y2 - y1
                if answer < width * height:
                    answer = width * height

            previous[y2] = (x1, y1, current_sum)
            idx += 1

        return answer