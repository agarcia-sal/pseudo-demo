from typing import List, Optional


def prod_signs(arrInts: List[int]) -> Optional[int]:
    def compute_sign(currIndex: int, accNegCount: int) -> int:
        if currIndex >= len(arrInts):
            return (-1) ** accNegCount
        elem = arrInts[currIndex]
        if elem < 0:
            return compute_sign(currIndex + 1, accNegCount + 1)
        return compute_sign(currIndex + 1, accNegCount)

    def accumulate_abs_total(idx: int, accSum: int) -> int:
        if idx >= len(arrInts):
            return accSum
        return accumulate_abs_total(idx + 1, accSum + abs(arrInts[idx]))

    if not arrInts:
        return None

    if any(elem == 0 for elem in arrInts):
        signProd = 0
    else:
        signProd = compute_sign(0, 0)

    magnitudeSum = accumulate_abs_total(0, 0)

    return signProd * magnitudeSum