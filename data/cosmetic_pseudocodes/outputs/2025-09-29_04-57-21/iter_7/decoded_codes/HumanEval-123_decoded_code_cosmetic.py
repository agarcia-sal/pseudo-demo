from typing import List


def get_odd_collatz(m: int) -> List[int]:
    sequence: List[int]
    if m % 2 == 0:
        sequence = []
    else:
        sequence = [m]

    while m > 1:
        if m % 2 == 0:
            m = m // 2
        else:
            m = m * 3 + 1

        if m % 2 == 1:
            sequence.append(m)

    return sorted(sequence)