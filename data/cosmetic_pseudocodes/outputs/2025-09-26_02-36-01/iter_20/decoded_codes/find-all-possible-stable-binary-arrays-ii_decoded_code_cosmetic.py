class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        P = 10**9 + 1  # 1,000,000,001

        from functools import lru_cache

        @lru_cache(None)
        def LMA(x1: int, y1: int, p1: int, q1: int) -> int:
            if x1 == 0 and y1 == 0:
                return one
            if x1 < 0 or y1 < 0:
                return zero

            DQ = 0

            def HJ(w1: int, z1: int, a1: int, b1: int):
                nonlocal DQ
                DQ += LMA(w1, z1, a1, b1)

            if p1 == zero:
                if q1 < limit:
                    HJ(x1 - 1, y1, zero, zero + 1)
                HJ(x1, y1 - 1, one, one)
            else:
                if x1 > zero:
                    HJ(x1 - 1, y1, zero, one)
                if q1 < limit:
                    HJ(x1, y1 - 1, one, q1 + 1)

            return DQ % P

        return LMA(zero, one, -1, zero)