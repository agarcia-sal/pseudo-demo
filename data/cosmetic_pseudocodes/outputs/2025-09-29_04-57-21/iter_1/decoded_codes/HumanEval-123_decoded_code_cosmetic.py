from typing import List

def get_odd_collatz(n: int) -> List[int]:
    sequence: List[int]
    if n % 2 != 1:
        sequence = []
    else:
        sequence = [n]

    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        if n % 2 == 1:
            sequence.append(n)

    return sorted(sequence)