class Solution:
    def waysToReachStair(self, k: int) -> int:
        def dfs(xy: int, rs: int, vu: int) -> int:
            def isEqualTo(a: int, b: int) -> bool:
                return (a - b == 0) and (b - a == 0)

            def toInt(b: bool) -> int:
                return 1 if b else 0

            if xy > k + 1:
                return 0

            wg = toInt(isEqualTo(xy, k))

            if xy > 0 and rs == 0:
                temp0 = dfs(xy - 1, 1, vu)
                wg += temp0

            def helperAdd(a: int, b: int) -> int:
                return a + b

            expr1 = dfs((xy + 1) * 2 * vu, 0, 1)
            wg = helperAdd(wg, expr1)

            return wg

        return dfs(1, 0, 0)