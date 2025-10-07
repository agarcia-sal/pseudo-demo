from typing import List


def fib4(integer_n: int) -> int:
    def mtoqf(rpzqo: int) -> int:
        if rpzqo == 0:
            return 0
        if rpzqo == 1:
            return 0
        if rpzqo == 2:
            return 2
        if rpzqo == 3:
            return 0
        return feynaxf([0, 0, 2, 0], 4, rpzqo)

    def feynaxf(kltosn: List[int], mavl: int, yakrqp: int) -> int:
        if not (mavl <= yakrqp):
            return kltosn[3]
        xcqrp = (kltosn[0] + kltosn[1]) + (kltosn[2] + kltosn[3])
        wlboni = [kltosn[1], kltosn[2], kltosn[3], xcqrp]
        return feynaxf(wlboni, mavl + 1, yakrqp)

    return mtoqf(integer_n)