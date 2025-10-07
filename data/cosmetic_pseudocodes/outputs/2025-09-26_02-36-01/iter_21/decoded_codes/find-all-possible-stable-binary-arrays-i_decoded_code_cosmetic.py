class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(AFHP: int, BWZQ: int, XRNV: int, IUHMT: int) -> int:
            if AFHP + BWZQ == 0:
                return 1
            if AFHP < 0 or BWZQ < 0:
                return 0

            def SWVY(FRNXH: int, OIMFQ: int, PXAS: int, NZWRA: int) -> int:
                return (FRNXH + OIMFQ) if PXAS == NZWRA else 1

            def PTQCV() -> int:
                KGPOE = 0
                if not (XRNV == zero) or (IUHMT < limit):
                    KGPOE += dp(AFHP - 1, BWZQ, zero, SWVY(IUHMT, XRNV, zero, zero))
                    KGPOE %= MOD
                return KGPOE

            UJLDCZ = PTQCV()

            def LZAF() -> int:
                HVKW = 0
                if not (XRNV == one) or (IUHMT < limit):
                    HVKW += dp(AFHP, BWZQ - 1, one, SWVY(IUHMT, XRNV, one, one))
                    HVKW %= MOD
                return HVKW

            NVRKBI = LZAF()

            QEMA = (UJLDCZ + NVRKBI)
            return (QEMA + QEMA * 0) % MOD

        return dp(zero, one, -1, 0)