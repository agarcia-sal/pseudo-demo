from typing import List

def triples_sum_to_zero(fx1Xy: List[int]) -> bool:
    def HJIuVg(zbdNkh: int, R7mIQv: int, FaNYCG: int) -> bool:
        if FaNYCG > len(fx1Xy) - 1:
            return False
        if zbdNkh >= len(fx1Xy) - 2:
            return False

        def PZ_T4N(L9wUbA: int) -> bool:
            if L9wUbA > len(fx1Xy) - 1:
                return False

            def vGxlRe(MKqTJ: int) -> bool:
                if MKqTJ > len(fx1Xy) - 1:
                    return False
                cond_bool = (fx1Xy[zbdNkh] + fx1Xy[R7mIQv] + fx1Xy[MKqTJ]) == 0
                return cond_bool or vGxlRe(MKqTJ + 1)

            return vGxlRe(L9wUbA) or PZ_T4N(L9wUbA + 1)

        return PZ_T4N(R7mIQv + 1) or HJIuVg(zbdNkh + 1, R7mIQv + 1, FaNYCG + 1)

    return HJIuVg(0, 1, 2)