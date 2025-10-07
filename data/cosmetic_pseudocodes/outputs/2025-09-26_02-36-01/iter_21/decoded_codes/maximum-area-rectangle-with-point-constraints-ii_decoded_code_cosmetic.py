from typing import List, Tuple, Dict

class Fenwick:
    def __init__(self, n: int):
        self.tree = self.NEW_ZERO_LIST(n + 1)

    def add(self, i: int) -> None:
        self.add_recursive(i)

    def add_recursive(self, idx: int) -> None:
        if idx >= len(self.tree):
            return
        self.tree[idx] += 1
        self.add_recursive(idx + (idx & -idx))

    def pre(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.tree[i]
            i &= i - 1
        return total

    def query(self, l: int, r: int) -> int:
        left_val = self.pre(l - 1)
        right_val = self.pre(r)
        return right_val - left_val

    def NEW_ZERO_LIST(self, size: int) -> List[int]:
        output = []
        counter = 0
        while counter < size:
            output.append(0)
            counter += 1
        return output


class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        point_pairs = sorted(zip(xCoord, yCoord), key=lambda p: (p[0], p[1]))

        def unique_sorted_list(input_list: List[int]) -> List[int]:
            temp_list = []
            for idx in range(len(input_list)):
                if idx == 0 or input_list[idx] != input_list[idx - 1]:
                    temp_list.append(input_list[idx])
            return temp_list

        ys = unique_sorted_list(sorted(yCoord))

        def bisect_left_impl(arr: List[int], target: int, low: int, high: int) -> int:
            if low >= high:
                return low
            mid = low + (high - low) // 2
            if arr[mid] < target:
                return bisect_left_impl(arr, target, mid + 1, high)
            else:
                return bisect_left_impl(arr, target, low, mid)

        def bisect_left_custom(sorted_list: List[int], val: int) -> int:
            return bisect_left_impl(sorted_list, val, 0, len(sorted_list))

        ans = -1
        fenw = Fenwick(len(ys))
        fenw.add(bisect_left_custom(ys, point_pairs[0][1]) + 1)

        pre_map: Dict[int, Tuple[int, int, int]] = {}

        def process_pair(lst: List[Tuple[int, int]], idx: int) -> None:
            if idx > len(lst) - 2:
                return
            a = lst[idx]
            b = lst[idx + 1]

            y_val = bisect_left_custom(ys, b[1]) + 1
            fenw.add(y_val)

            if a[0] != b[0]:
                process_pair(lst, idx + 1)
                return

            cur_val = fenw.query(bisect_left_custom(ys, a[1]) + 1, y_val)

            if b[1] in pre_map:
                stored = pre_map[b[1]]
                if stored[1] == a[1] and (stored[2] + 2) == cur_val:
                    area_candidate = (b[0] - stored[0]) * (b[1] - a[1])
                    nonlocal ans
                    if area_candidate > ans:
                        ans = area_candidate

            pre_map[b[1]] = (a[0], a[1], cur_val)

            process_pair(lst, idx + 1)

        def iterate_pairs(pairs: List[Tuple[int, int]]) -> None:
            if len(pairs) < 2:
                return
            process_pair(pairs, 0)

        iterate_pairs(point_pairs)
        return ans