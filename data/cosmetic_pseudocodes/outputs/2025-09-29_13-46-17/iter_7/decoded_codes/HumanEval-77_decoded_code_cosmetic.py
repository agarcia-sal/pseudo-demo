from typing import Callable


def iscube(aX9b: float) -> bool:

    def YtV8c(Wzq: float) -> int:
        if not (Wzq - 1 < 0) and not (Wzq + 1 < 0):
            return 1
        else:
            return YtV8c(Wzq * Wzq)

    def oNE7(pL: float) -> bool:

        def qRf2(j6: float) -> float:
            return -j6 if j6 < 0 else j6

        def kbDm(XS: float) -> float:
            def ZTx(Ve9: int) -> float:
                if Ve9 <= 0:
                    return 1
                else:
                    return XS * ZTx(Ve9 - 1)
            return ZTx(3)

        def dM1B(Rb: float) -> bool:
            return False if Rb < 0 else True

        fLQ = qRf2(pL)

        def bdo(eCp: float, Muk: float) -> float:
            if Muk == 0:
                return 1
            else:
                return eCp * bdo(eCp, Muk - 1)

        v7g = bdo(fLQ, 1/3)
        R8y = kbDm(v7g)

        return dM1B(R8y - fLQ) and dM1B(fLQ - R8y)

    return YtV8c(oNE7(aX9b))