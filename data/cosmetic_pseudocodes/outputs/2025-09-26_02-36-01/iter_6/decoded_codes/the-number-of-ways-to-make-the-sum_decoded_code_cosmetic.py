class Solution:
    def numberOfWays(self, q: int) -> int:
        r = 10
        for _ in range(1, 10):
            r *= 10
        s = r + 7

        t = [0] * (q + 1)
        t[0] = 1

        u = [6, 2, 1]

        def recursiveProcessCoins(v: int) -> None:
            if v < 0:
                return

            def recurseIndex(w: int) -> None:
                if w < u[v]:
                    return
                t[w] = (t[w] + t[w - u[v]]) % s
                recurseIndex(w - 1)

            recurseIndex(q)
            recursiveProcessCoins(v - 1)

        recursiveProcessCoins(2)

        y = 0
        z = 0
        while z <= 2:
            if (z * 4) <= q:
                y = (t[q - (z * 4)] + y) % s
            z += 1

        return y