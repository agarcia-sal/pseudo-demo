class Solution:
    def numberOfStableArrays(self, a: int, b: int, c: int) -> int:
        P = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def recur(x: int, y: int, prev: int, streak: int) -> int:
            if x == 0 and y == 0:
                return b
            if x < 0 or y < 0:
                return a

            acc = a
            if prev == a:
                if streak < c:
                    acc += recur(x - 1, y, a, streak + 1)
                acc += recur(x, y - 1, b, a)
            else:
                if x > a:
                    acc += recur(x - 1, y, a, b)
                if streak < c:
                    acc += recur(x, y - 1, b, streak + 1)

            return acc % P

        return recur(a, b - 1, a, a)