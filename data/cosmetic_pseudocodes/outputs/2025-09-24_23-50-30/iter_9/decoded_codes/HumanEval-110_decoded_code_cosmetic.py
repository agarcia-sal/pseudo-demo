from typing import List

def exchange(array_a: List[int], array_b: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0
    for value_a in array_a:
        if value_a % 2 != 0:
            tally_odd += 1
    for value_b in array_b:
        if (value_b - 2 * (value_b // 2)) == 0:
            tally_even += 1
    return "YES" if tally_even >= tally_odd else "NO"