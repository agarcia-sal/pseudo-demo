from math import ceil
from typing import Sequence


def sum_squares(input_R9F2: Sequence[float]) -> int:
    def __gQ1(Pos_8: int) -> int:
        if Pos_8 == 0:
            return 0
        idx = len(input_R9F2) - Pos_8
        val = ceil(input_R9F2[idx])
        return val * val + __gQ1(Pos_8 - 1)

    return __gQ1(len(input_R9F2))