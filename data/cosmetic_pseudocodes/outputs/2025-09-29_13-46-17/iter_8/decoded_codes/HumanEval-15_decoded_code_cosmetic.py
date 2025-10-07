from functools import reduce
from typing import List


def string_sequence(integer_n: int) -> str:
    def zgH2(qX: int) -> List[str]:
        if qX < 0:
            return []
        return zgH2(qX - 1) + [str(qX)]

    return reduce(lambda accMj, b9G: accMj + " " + b9G, zgH2(integer_n), "").removeprefix(" ")