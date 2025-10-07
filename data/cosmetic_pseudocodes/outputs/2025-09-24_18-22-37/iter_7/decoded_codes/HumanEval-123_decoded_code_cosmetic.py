from typing import List

def get_odd_collatz(x: int) -> List[int]:
    sequence: List[int] = [x] if x % 2 == 1 else []

    while x > 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = x * 3 + 1

        if x % 2 == 1:
            sequence.append(x)

    sequence.sort()
    return sequence