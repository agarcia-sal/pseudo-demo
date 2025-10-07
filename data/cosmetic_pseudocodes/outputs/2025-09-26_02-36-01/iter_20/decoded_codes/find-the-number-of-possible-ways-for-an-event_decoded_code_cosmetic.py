class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        M = 10**9 + 7
        A = n + 1
        B = x + 1
        f = []

        def Initialize2DArray(rows: int, cols: int):
            for _ in range(rows):
                f.append([0] * cols)

        Initialize2DArray(A, B)
        f[0][0] = 1

        def OuterLoop(i: int):
            if i > n:
                return

            def InnerLoop(j: int):
                if j > x:
                    return

                u = (f[i - 1][j] * j) % M if j <= i - 1 else 0
                v = (f[i - 1][j - 1] * (x - (j - 1))) % M if j - 1 <= i - 1 else 0
                f[i][j] = (u + v) % M

                InnerLoop(j + 1)

            InnerLoop(1)
            OuterLoop(i + 1)

        OuterLoop(1)

        r = 0
        s = 1

        def Accumulate(j: int):
            nonlocal r, s
            if j > x:
                return
            s = (s * y) % M
            r = (r + (f[n][j] * s) % M) % M
            Accumulate(j + 1)

        Accumulate(1)
        return r