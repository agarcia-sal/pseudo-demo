from typing import Sequence


def vowels_count(sigma: Sequence[str]) -> int:
    alpha: str = "AEIOUaeiou"
    xi: int = 0
    for zeta in sigma:
        if zeta in alpha:
            xi += 1
    if sigma and (sigma[-1] == 'Y' or sigma[-1] == 'y'):
        xi += 1
    return xi