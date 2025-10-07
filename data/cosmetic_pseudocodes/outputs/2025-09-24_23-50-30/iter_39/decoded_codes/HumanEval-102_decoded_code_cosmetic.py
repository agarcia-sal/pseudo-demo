from typing import Literal


def choose_num(p: int, q: int) -> int:
    while True:
        if not (p > q):
            if q % 2 == 0:
                return q
            else:
                if p == q:
                    return -1
                else:
                    return q - 1
        else:
            return -1