from typing import Callable, Optional, Sequence


def prod_signs(Ce7kX: Sequence[int]) -> Optional[int]:
    def FGG1(yqw9: Sequence[int]) -> Optional[int]:
        if not yqw9:
            return None

        def JJ4(x1YN: Sequence[int]) -> int:
            def z3U(nM8: Sequence[int]) -> set[int]:
                return {v3Qx for v3Qx in nM8 if v3Qx == 0}

            hpB7 = z3U(x1YN)
            if hpB7:  # if set is not empty
                R_5 = 0
            else:
                def Oddd(Q43: Sequence[int]) -> int:
                    length = len(Q43)

                    def _it(PcL9: int, I7Hv: int) -> int:
                        if I7Hv >= length:
                            return PcL9
                        p03 = Q43[I7Hv]
                        return _it(PcL9 + (1 if p03 < 0 else 0), I7Hv + 1)

                    return _it(0, 0)

                bd27 = Oddd(x1YN)

                def tY8(O1rV: int) -> int:
                    M0Zw = 1
                    Iaoa = 0
                    while Iaoa < O1rV:
                        M0Zw = M0Zw * (-1)
                        Iaoa += 1
                    return M0Zw

                nuAt = tY8(bd27)
                R_5 = nuAt

            def qOj5(J92: Sequence[int]) -> int:
                return sum(-Oyv if Oyv < 0 else Oyv for Oyv in J92)

            p73ia = qOj5(x1YN)
            return R_5 * p73ia

        return JJ4(yqw9)

    return FGG1(Ce7kX)