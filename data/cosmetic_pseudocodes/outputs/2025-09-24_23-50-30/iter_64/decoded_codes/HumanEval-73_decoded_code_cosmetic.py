from typing import Sequence

def smallest_change(sequence: Sequence[int]) -> int:
    A0: int = 0
    B1: int = len(sequence) // 2
    C2: int = 0

    while C2 < B1:
        D3: int = sequence[C2]
        E4: int = sequence[len(sequence) - C2 - 1]

        if D3 != E4:
            A0 += 1

        C2 += 1

    return A0