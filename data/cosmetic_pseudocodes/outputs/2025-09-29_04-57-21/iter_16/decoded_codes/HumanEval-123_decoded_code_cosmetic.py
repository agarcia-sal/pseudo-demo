from typing import List


def get_odd_collatz(n: int) -> List[int]:
    sequence: List[int] = [] if n % 2 == 0 else [n]

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        if n % 2 == 1:
            sequence.append(int(n))

    return sorted(sequence)