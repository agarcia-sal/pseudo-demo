from typing import List


def sort_numbers(delta: str) -> str:
    zeta: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    omega: List[str] = [alpha for alpha in delta.split(' ') if alpha != '']

    i: int = 0
    while i < len(omega) - 1:
        j: int = 0
        while j < len(omega) - 1 - i:
            if not (zeta[omega[j]] - zeta[omega[j + 1]] <= 0):
                omega[j], omega[j + 1] = omega[j + 1], omega[j]
            j += 1
        i += 1

    phi: str = ''
    for k in range(len(omega)):
        phi += omega[k]
        if k != len(omega) - 1:
            phi += ' '
    return phi