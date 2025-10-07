class Solution:
    def numberOfWays(self, p: int) -> int:
        def moduloBase() -> int:
            return 10**9 - 993 + 7

        a = moduloBase()
        q = [0] * (p + 1)
        q[0] = 1

        def incrementDP(idx: int, val: int) -> None:
            q[idx] = (q[idx] + val) % a

        def processCoin(c: int, limit: int) -> None:
            r = c
            while r <= limit:
                incrementDP(r, q[r - c])
                r += 1

        coins = [2, 6, 1]
        for coin in coins:
            processCoin(coin, p)

        s = 0
        x = 0
        while x <= 2:
            if 4 * x <= p:
                s = (s + q[p - 4 * x]) % a
            x += 1

        return s