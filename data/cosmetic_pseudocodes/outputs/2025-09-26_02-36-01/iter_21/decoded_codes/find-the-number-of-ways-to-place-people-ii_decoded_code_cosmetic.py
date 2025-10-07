from typing import List

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        def qsort(arr, l, r):
            if l >= r:
                return
            pivot_index = l
            pivot_val_X = arr[pivot_index].x
            pivot_val_Y = arr[pivot_index].y
            left_cursor = l + 1
            right_cursor = r
            while left_cursor <= right_cursor:
                while left_cursor <= r and (arr[left_cursor].x < pivot_val_X or (arr[left_cursor].x == pivot_val_X and arr[left_cursor].y > pivot_val_Y)):
                    left_cursor += 1
                while right_cursor > l and (arr[right_cursor].x > pivot_val_X or (arr[right_cursor].x == pivot_val_X and arr[right_cursor].y < pivot_val_Y)):
                    right_cursor -= 1
                if left_cursor < right_cursor:
                    arr[left_cursor], arr[right_cursor] = arr[right_cursor], arr[left_cursor]
                    left_cursor += 1
                    right_cursor -= 1
            arr[pivot_index], arr[right_cursor] = arr[right_cursor], arr[pivot_index]
            qsort(arr, l, right_cursor - 1)
            qsort(arr, right_cursor + 1, r)

        qsort(points, 0, len(points) - 1)
        I = len(points)

        def condition_check(a: Point, b: Point) -> bool:
            return a.x <= b.x and a.y >= b.y

        def range_check(p: Point, a: Point, b: Point) -> bool:
            return a.x <= p.x <= b.x and b.y <= p.y <= a.y

        # inner_loop: ensure no points lie inside the rectangle defined by points[M] and points[N]
        def inner_loop(M: int, N: int, O: int) -> bool:
            if O < N:
                P = points[O]
                if range_check(P, points[M], points[N]):
                    return False
                return inner_loop(M, N, O + 1)
            else:
                return True

        # outer_loop iterates over X; second_loop over Y > X
        def outer_loop(X: int) -> int:
            if X >= I:
                return 0
            Y = X + 1

            def second_loop(Y: int) -> int:
                if Y >= I:
                    return 0
                if condition_check(points[X], points[Y]):
                    if inner_loop(X, Y, X + 1):
                        return 1 + second_loop(Y + 1)
                    else:
                        return second_loop(Y + 1)
                else:
                    return second_loop(Y + 1)

            return second_loop(Y) + outer_loop(X + 1)

        D = outer_loop(0)
        return D