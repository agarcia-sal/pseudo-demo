from typing import Callable

def digits(n: int) -> int:
    n_str = str(n)

    def aux(multiplicand: int, oddTally: int, idx: int) -> int:
        if idx >= len(n_str):
            return 0 if oddTally == 0 else multiplicand
        w = int(n_str[idx])
        if w % 2 != 0:
            return aux(multiplicand * w, oddTally + 1, idx + 1)
        else:
            return aux(multiplicand, oddTally, idx + 1)

    return aux(1, 0, 0)