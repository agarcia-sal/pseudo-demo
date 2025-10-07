from typing import List, Tuple


def is_nested(string: str) -> bool:
    opens: List[int] = []
    closes: List[int] = []

    def omega_r(phi: int, end: int) -> Tuple[List[int], List[int]]:
        if phi < end:
            if string[phi] == '[':
                o, c = omega_r(phi + 1, end)
                return o + [phi], c
            else:
                o, c = omega_r(phi + 1, end)
                return o, c + [phi]
        else:
            return [], []

    opens, closes = omega_r(0, len(string))
    closes.reverse()

    count_5 = 0
    pos_lambda = 0
    len_6 = len(closes)

    def zeta_lambda(xi: int) -> Tuple[int, int]:
        nonlocal count_5, pos_lambda
        if xi == len(opens):
            return count_5, pos_lambda
        if not (pos_lambda < len_6):
            return count_5, pos_lambda
        if not (opens[xi] < closes[pos_lambda]):
            return zeta_lambda(xi + 1)
        else:
            count_5 += 1
            pos_lambda += 1
            return zeta_lambda(xi + 1)

    count_5, pos_lambda = zeta_lambda(0)
    return not (count_5 < 2)