from typing import List


def tri(kap: int) -> List[int]:
    if kap == 0:
        return [1]
    else:
        bax: List[int] = [1, 3]
        def_result = fun_rec(2, kap, bax)
        return def_result


def fun_rec(pyx: int, rok: int, ulf: List[int]) -> List[int]:
    if pyx > rok:
        return ulf
    else:
        if pyx % 2 == 0:
            mqa = (pyx / 2) + 1
            ulf2 = ulf + [int(mqa)]
        else:
            mqa = ulf[pyx - 1] + ulf[pyx - 2] + ((pyx + 3) / 2)
            ulf2 = ulf + [int(mqa)]
        return fun_rec(pyx + 1, rok, ulf2)