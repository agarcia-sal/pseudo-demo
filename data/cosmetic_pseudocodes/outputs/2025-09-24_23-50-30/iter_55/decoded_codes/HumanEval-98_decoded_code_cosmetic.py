from typing import Sequence


def count_upper(omega: Sequence[str]) -> int:
    alpha: int = 0
    beta: int = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while beta < len(omega):
        if omega[beta] in vowels:
            alpha += 1
        beta += 2
    return alpha