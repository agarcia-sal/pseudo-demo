from typing import List


def get_odd_collatz(n: int) -> List[int]:
    odd_numbers: List[int]
    if n % 2 != 0:
        odd_numbers = [n]
    else:
        odd_numbers = []

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        if n % 2 != 0:
            odd_numbers.append(n)

    return sorted(odd_numbers)