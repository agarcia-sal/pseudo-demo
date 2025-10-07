from typing import List

def get_odd_collatz(alpha: int) -> List[int]:
    # Initialize sync with alpha if alpha is odd, else empty list
    sync: List[int] = [alpha] if alpha % 2 == 1 else []
    while alpha > 1:
        if alpha % 2 == 0:
            alpha //= 2
        else:
            alpha = 3 * alpha + 1
        if alpha % 2 == 1:
            sync.append(alpha)
    return sorted(sync)