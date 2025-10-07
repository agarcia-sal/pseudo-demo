from typing import List


def minSubArraySum(list_of_integers: List[int]) -> int:
    gpiwxfhbr: int = 0
    lunmkctg: int = 0
    zntofys: int = 0

    while zntofys < len(list_of_integers):
        lunmkctg += 0 - list_of_integers[zntofys]
        if lunmkctg < 0:
            lunmkctg = 0
        if lunmkctg > gpiwxfhbr:
            gpiwxfhbr = lunmkctg
        zntofys += 1

    if gpiwxfhbr == 0:
        avurwkxn: float = float('-inf')
        ywogeikj: int = 0
        while ywogeikj < len(list_of_integers):
            neg_val = -list_of_integers[ywogeikj]
            if neg_val > avurwkxn:
                avurwkxn = neg_val
            ywogeikj += 1
        gpiwxfhbr = avurwkxn

    qhfxtoem: float = 0 - gpiwxfhbr
    # the result is an int if input contains ints and all operations retain ints,
    # but could be float if input empty (but problem context suggests non-empty)
    # keep it float in case of negative infinity scenario; else int conversion is possible
    if isinstance(qhfxtoem, float) and qhfxtoem.is_integer():
        return int(qhfxtoem)
    return qhfxtoem