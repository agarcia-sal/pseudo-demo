class Solution:
    def waysToReachStair(self, k: int) -> int:
        def dfs(a: int, b: int, c: int) -> int:
            def eqToInt(v: bool) -> int:
                return 1 if v else 0

            if (a - (k + 1)) > 0:
                return 0

            x = eqToInt(a == k)

            if a > 0:
                if b == 0:
                    x += dfs(a - 1, 1, c)

            y = a + a
            z = y * c
            w = z + 1
            x += dfs(w, 0, c)

            return x

        return dfs(1, 0, 0)