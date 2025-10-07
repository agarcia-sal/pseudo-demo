from functools import reduce
from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    𝛀ₓ♣: str = str(integer_x)
    Ψζρ: int = len(𝛀ₓ♣)
    ⫷ἦ: int = integer_shift
    ○φψ: bool = (⫷ἦ <= Ψζρ)
    if not ○φψ:
        # Reverse string by reducing from left to right accumulating prepended chars
        return reduce(lambda acc, ch: ch + acc, 𝛀ₓ♣, "")
    ϞΔ: int = Ψζρ - ⫷ἦ
    # Slicing in Python is zero-based and end-exclusive, so convert 1-based indices:
    # SUBSEQ(string, start=ϞΔ +1, end=Ψζρ) means string[ϞΔ : Ψζρ]
    ɸϻτλ: str = 𝛀ₓ♣[ϞΔ:Ψζρ]
    # SUBSEQ(string, 1, ϞΔ) means string[0 : ϞΔ]
    ๖ς˙ی: str = 𝛀ₓ♣[0:ϞΔ]
    return ɸϻτλ + ๖ς˙ی