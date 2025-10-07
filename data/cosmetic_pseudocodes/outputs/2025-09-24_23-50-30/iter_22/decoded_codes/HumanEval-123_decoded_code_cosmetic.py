from typing import List

def get_odd_collatz(x: int) -> List[int]:
    seq: List[int] = [x] if x % 2 != 0 else []
    y: int = x
    while y > 1:
        if y % 2 == 0:
            y //= 2
        else:
            y = 3 * y + 1
        if y % 2 != 0:
            seq.append(y)
    return sorted(seq)