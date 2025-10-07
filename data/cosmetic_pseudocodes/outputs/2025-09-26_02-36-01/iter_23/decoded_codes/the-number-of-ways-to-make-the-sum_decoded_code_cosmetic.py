class Solution:
    def numberOfWays(self, n: int) -> int:
        g = 10**9 + 7
        t = [0] * (n + 1)
        t[0] = 1

        # recB(idxB, limitC): updates t[idxB] using t[idxB - p] recursively
        def recB(idxB, limitC, p):
            if idxB > limitC:
                return
            t[idxB] = (t[idxB] + t[idxB - p]) % g
            recB(idxB + 1, limitC, p)

        # recA(idxA, limitA, coinA): for each idxA, sets p=coinA and calls recB
        def recA(idxA, limitA, coinA):
            if idxA > limitA:
                return
            p = coinA
            recB(idxA, limitA, p)
            recA(idxA + 1, limitA, coinA)

        coins = [1, 2, 6]

        # iterCoins(pos): iterates over coins, calls recA
        def iterCoins(pos):
            if pos > len(coins):
                return
            q = coins[pos - 1]
            recA(q, n, q)
            iterCoins(pos + 1)

        iterCoins(1)

        r = 0

        # recK(k): updates r based on t[n - k*4] for k in [0..2]
        def recK(k):
            nonlocal r
            if k > 2:
                return
            if k * 4 <= n:
                r = (r + t[n - k * 4]) % g
            recK(k + 1)

        recK(0)

        return r