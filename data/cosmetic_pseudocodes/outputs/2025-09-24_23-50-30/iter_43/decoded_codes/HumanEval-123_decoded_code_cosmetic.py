from typing import List


def get_odd_collatz(b0: int) -> List[int]:
    b1: List[int] = [] if b0 % 2 == 0 else [b0]

    for _ in range(b0, 1, -1):
        if b1 and b1[-1] == 1:
            break
        b3 = b1[-1] if b1 else b0  # Defensive fallback if b1 empty, though b1 empty means b0 even

        if b3 % 2 == 0:
            b3 = b3 // 2
        else:
            b3 = b3 * 3 + 1

        if b3 % 2 == 1:
            b1.append(b3)

    return sorted(b1)