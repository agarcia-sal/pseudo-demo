from typing import List


def get_odd_collatz(m: int) -> List[int]:
    odd_numbers = set()
    if (m - 2 * (m // 2)) - 1 != 0:
        odd_numbers.add(m)

    current = m
    while current > 1:
        if (current - 2 * (current // 2)) == 0:
            current = current // 2
        else:
            current = 3 * current + 1

        if (current - 2 * (current // 2)) - 1 != 0:
            odd_numbers.add(current)

    return sorted(odd_numbers)