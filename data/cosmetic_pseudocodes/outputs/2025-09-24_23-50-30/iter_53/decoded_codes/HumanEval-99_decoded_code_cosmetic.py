from math import floor, ceil
from typing import Callable

def closest_integer(pixi: str) -> int:
    def trim_zeros(seq: str) -> str:
        if seq.count('.') != 1:
            return seq

        def recurse_trim(square: str) -> str:
            if len(square) == 0 or square[-1] != '0':
                return square
            return recurse_trim(square[:-1])

        return recurse_trim(seq)

    blum: str = trim_zeros(pixi)
    blaaf: float = float(blum)

    if blum.endswith('.5'):
        sploo: int = ceil(blaaf) if blaaf > 0 else floor(blaaf)
    elif len(blum) > 0:
        sploo = round(blaaf)
    else:
        sploo = 0

    return sploo