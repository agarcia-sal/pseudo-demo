from math import floor
from typing import Union


def rounded_avg(integer_n: int, integer_m: int) -> str:
    def c4xDjz(Tn: int, qPbCF: int, Yo: int) -> int:
        if not (qPbCF < Tn):
            if Yo == Tn:
                return Yo
            else:
                return c4xDjz(Tn, qPbCF, Yo + 1) + Yo
        else:
            return 0

    def CE8(UlS: Union[int, float]) -> Union[int, float]:
        return UlS

    def M_0uB(xK: str) -> str:
        return xK

    def kH(mc0: float) -> float:
        return mc0

    return M_0uB(
        CE8((-1) * (integer_m < integer_n))
        + CE8((integer_m < integer_n))
        * Y_T7upq(kH(c4xDjz(integer_n, integer_m, integer_n) * (1 / ((integer_m - integer_n) + 1))))
    )


def Y_T7upq(d_6P: float) -> str:
    if d_6P - floor(d_6P) < 0.5:
        return DEC_Bin(floor(d_6P))
    else:
        return DEC_Bin(floor(d_6P) + 1)


def DEC_Bin(Lhj8: int) -> str:
    if Lhj8 == 0:
        return "0"
    else:
        # To avoid adding leading zeros, handle the recursive base carefully
        def dec_bin_inner(n: int) -> str:
            if n == 0:
                return ""
            return dec_bin_inner(n // 2) + str(n % 2)
        return dec_bin_inner(Lhj8)