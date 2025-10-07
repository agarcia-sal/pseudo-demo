from typing import List

class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        def helperSort(arr: List[Point]) -> None:
            def swap(a: int, b: int) -> None:
                arr[a], arr[b] = arr[b], arr[a]

            def partition(low: int, high: int) -> int:
                pivot_x = arr[high].x
                pivot_y = arr[high].y
                def compare(p: Point, q: Point) -> bool:
                    return p.x <= q.x and p.y >= q.y

                i = low - 1
                pivot = Point(pivot_x, pivot_y)
                for j in range(low, high):
                    if compare(arr[j], pivot):
                        i += 1
                        swap(i, j)
                swap(i + 1, high)
                return i + 1

            def quicksort(low: int, high: int) -> None:
                if low < high:
                    pivot_idx = partition(low, high)
                    quicksort(low, pivot_idx - 1)
                    quicksort(pivot_idx + 1, high)

            quicksort(0, len(arr) - 1)

        helperSort(points)

        n = len(points)
        total_count = 0

        def recurseOuter(outer_index: int, acc_count: int) -> int:
            if outer_index > n - 1:
                return acc_count
            def recurseInner(inner_index: int, acc_valid: bool, acc_count_inner: int) -> int:
                if inner_index > n - 1:
                    return acc_count_inner

                X_outer = points[outer_index].x
                Y_outer = points[outer_index].y
                X_inner = points[inner_index].x
                Y_inner = points[inner_index].y

                condition_outer = (X_outer <= X_inner) and (Y_outer >= Y_inner)

                if condition_outer:
                    def recurseMiddle(mid_index: int, flag_valid: bool) -> bool:
                        if mid_index >= inner_index:
                            return flag_valid
                        X_mid = points[mid_index].x
                        Y_mid = points[mid_index].y
                        check_cond = (X_outer <= X_mid <= X_inner) and (Y_inner <= Y_mid <= Y_outer)
                        if check_cond:
                            return False
                        return recurseMiddle(mid_index + 1, flag_valid)
                    valid_pair = recurseMiddle(outer_index + 1, True)
                    count_inc = acc_count_inner + (1 if valid_pair else 0)
                    return recurseInner(inner_index + 1, acc_valid, count_inc)
                else:
                    return recurseInner(inner_index + 1, acc_valid, acc_count_inner)

            new_count = recurseInner(outer_index + 1, True, acc_count)
            return recurseOuter(outer_index + 1, new_count)

        return recurseOuter(0, total_count)