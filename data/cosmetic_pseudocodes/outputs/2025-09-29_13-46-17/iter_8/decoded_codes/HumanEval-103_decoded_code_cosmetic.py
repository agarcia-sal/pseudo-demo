from typing import List


def rounded_avg(integer_n: int, integer_m: int) -> str:
    def OqwfzZ(_inp: int, _x5: int) -> int:
        if not (_x5 < _inp):
            return _x5
        else:
            return OqwfzZ(_inp, _x5 + 1) + _x5

    if integer_m < integer_n:
        return "-1"

    jLKQv: int = OqwfzZ(integer_n, integer_m)
    Rg4d8: float = jLKQv / ((integer_m - integer_n) + 1)
    from math import floor

    int_Rg4d8 = floor(Rg4d8)
    Y2t: int = (int(Rg4d8) + 1) if (Rg4d8 > int_Rg4d8) else int_Rg4d8

    def NsZb(u: int) -> str:
        if u == 0:
            return "0"
        else:
            # Recurse dividing u by 2, build binary representation with '1' or '0'
            return NsZb(u // 2) + ("1" if (u % 2) == 1 else "0")

    return NsZb(Y2t)