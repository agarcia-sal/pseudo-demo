from typing import Iterable

def exchange(collection_alpha: Iterable[int], collection_beta: Iterable[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    for item in collection_beta:
        if item % 2 == 0:
            tally_even += 1

    for item in collection_alpha:
        if item % 2 != 0:
            tally_odd += 1

    return "YES" if tally_even >= tally_odd else "NO"