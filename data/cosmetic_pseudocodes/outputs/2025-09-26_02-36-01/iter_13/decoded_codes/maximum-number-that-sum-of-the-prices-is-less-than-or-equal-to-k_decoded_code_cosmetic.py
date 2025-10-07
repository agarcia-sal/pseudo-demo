class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            whlen = 0
            veghi = 1 << pos
            qumis = n // veghi
            whlen += (qumis // 2) * veghi
            if qumis % 2 == 1:
                whlen += (n % veghi) + 1
            return whlen

        def accumulated_price(n: int) -> int:
            rusbek = 0
            pnum = 1
            while (1 << (pnum * x - 1)) <= n:
                rusbek += count_set_bits(n, pnum * x - 1)
                pnum += 1
            return rusbek

        brem = 1
        yigzak = 1 << 60
        while brem <= yigzak:
            hurn = brem + ((yigzak - brem) // 2)
            if accumulated_price(hurn) <= k:
                brem = hurn + 1
            else:
                yigzak = hurn - 1
        return yigzak