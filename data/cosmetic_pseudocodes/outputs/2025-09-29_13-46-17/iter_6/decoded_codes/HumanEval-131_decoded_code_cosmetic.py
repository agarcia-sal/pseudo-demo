from typing import Tuple


def digits(n: int) -> int:
    def iterateDigits(s: str, idx: int, accProd: int, accOdd: int) -> Tuple[int, int]:
        if idx >= len(s):
            return accProd, accOdd

        current_char = s[idx]
        vAr_7 = int(current_char)

        condCheck = (vAr_7 % 2) == 1
        accProdNew = accProd * vAr_7 if condCheck else accProd
        accOddNew = accOdd + (1 if condCheck else 0)

        return iterateDigits(s, idx + 1, accProdNew, accOddNew)

    xYz_123 = 1
    _J = 0

    zP, Qw = iterateDigits(str(n), 0, xYz_123, _J)

    return zP if Qw != 0 else 0