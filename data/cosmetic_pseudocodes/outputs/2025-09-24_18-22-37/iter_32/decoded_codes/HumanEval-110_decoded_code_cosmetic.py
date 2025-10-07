from typing import List, Union

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    idx_a: int = 0
    while idx_a < len(list_one):
        item_a: int = list_one[idx_a]
        if item_a % 2 != 0:
            tally_odd += 1
        idx_a += 1

    idx_b: int = 0
    while idx_b < len(list_two):
        item_b: int = list_two[idx_b]
        if item_b % 2 == 0:
            tally_even += 1
        idx_b += 1

    if not (tally_even < tally_odd):
        return "YES"
    else:
        return "NO"