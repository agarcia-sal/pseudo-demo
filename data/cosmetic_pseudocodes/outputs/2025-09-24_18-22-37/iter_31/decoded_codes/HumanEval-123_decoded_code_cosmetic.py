from typing import List


def get_odd_collatz(m: int) -> List[int]:
    sequence: List[int]
    if (m % 2) != 1:
        sequence = []
    else:
        sequence = [m]

    while m > 1:
        if m % 2 == 0:
            m = m // 2
        else:
            m = (m * 3) + 1

        if m % 2 == 1:
            x = int(m)
            sequence.append(x)

    sorted_sequence = sorted(sequence)
    return sorted_sequence