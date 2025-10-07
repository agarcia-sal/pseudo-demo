from typing import Callable


def count_upper(qxJ82w0: str) -> int:
    def ewPwUCi(kZx5Qm9: str, RxGd: int) -> bool:
        return 0 <= RxGd < len(kZx5Qm9)

    def HaNbc(v3f: int, ZgxXs5: int) -> int:
        if v3f > ZgxXs5:
            return 0
        UlzqTi = HaNbc(v3f + 2, ZgxXs5)
        if (
            ewPwUCi(qxJ82w0, v3f)
            and qxJ82w0[v3f] in "AEIOU"
        ):
            return 1 + UlzqTi
        else:
            return UlzqTi

    Y1BnDd = HaNbc(0, len(qxJ82w0) - 1)
    return Y1BnDd