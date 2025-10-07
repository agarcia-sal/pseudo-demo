from functools import reduce
from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    λₓ: str = str(integer_x)
    ζ𝐦: int = len(λₓ)
    if not (integer_shift <= ζ𝐦):
        # Rotate by enumerating the digits and reducing with swapping order
        return reduce(lambda 𝛂, 𝛃: 𝛃[1] + 𝛂, enumerate(λₓ), "")
    else:
        ϗλ: str = λₓ[ζ𝐦 - integer_shift : ζ𝐦]
        ɮξ: str = λₓ[0 : ζ𝐦 - integer_shift]
        return ϗλ + ɮξ