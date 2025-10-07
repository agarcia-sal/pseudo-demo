from typing import Sequence

def hex_key(omega: Sequence[str]) -> int:
    sigma = {'2', '3', '5', '7', 'B', 'D'}
    delta = 0
    beta = 0
    while beta < len(omega):
        epsilon = omega[beta]
        if epsilon in sigma:
            delta += 1
        beta += 1
    return delta