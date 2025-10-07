from typing import List

def get_odd_collatz(m: int) -> List[int]:
    sequence = set()
    if m % 2 != 0:
        sequence.add(m)

    while m > 1:
        m = m // 2 if m % 2 == 0 else 3 * m + 1
        if m % 2 == 1:
            sequence.add(m)

    return sorted(sequence)