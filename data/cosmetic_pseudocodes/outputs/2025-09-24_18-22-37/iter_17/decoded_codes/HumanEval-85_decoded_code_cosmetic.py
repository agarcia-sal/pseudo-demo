from typing import Sequence

def add(omega: Sequence[int]) -> int:
    productive_sum: int = 0
    idx: int = 0
    max_index: int = len(omega)
    while idx < max_index:
        element_at_idx: int = omega[idx]
        if element_at_idx % 2 == 0:
            productive_sum += element_at_idx
        idx += 2
    return productive_sum