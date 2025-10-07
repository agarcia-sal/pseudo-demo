from typing import List


def get_odd_collatz(value: int) -> List[int]:
    odd_terms: List[int] = [] if value % 2 == 0 else [value]

    while value > 1:
        if value % 2 == 0:
            value //= 2
        else:
            value = value * 3 + 1

        if value % 2 == 1:
            odd_terms.append(int(value))

    return sorted(odd_terms)