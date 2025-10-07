from typing import List


def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    for candidate in array_alpha:
        if candidate & 1 == 1:
            tally_odd += 1

    for candidate in array_beta:
        if (candidate & 1) == 0:
            tally_even += 1

    if tally_even < tally_odd:
        return "NO"
    else:
        return "YES"