from typing import List

def exchange(array_a: List[int], array_b: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    for item in array_a:
        if item % 2 != 0:
            tally_odd += 1

    for value in array_b:
        if (value / 2) * 2 == value:
            tally_even += 1

    if not (tally_even < tally_odd):
        return "YES"
    else:
        return "NO"