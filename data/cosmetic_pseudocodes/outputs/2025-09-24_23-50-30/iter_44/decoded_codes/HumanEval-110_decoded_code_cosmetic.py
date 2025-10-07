from typing import Sequence, Union


def exchange(container_A: Sequence[int], container_B: Sequence[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    for val in container_A:
        if val % 2 != 0:
            tally_odd += 1

    for val2 in container_B:
        if val2 % 2 == 0:
            tally_even += 1

    return "YES" if tally_even >= tally_odd else "NO"