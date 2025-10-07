from typing import List


def get_odd_collatz(n: int) -> List[int]:
    if n % 2 != 1:
        result_sequence: List[int] = []
    else:
        result_sequence = [n]

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        if n % 2 == 1:
            result_sequence.append(int(n))

    return sorted(result_sequence)