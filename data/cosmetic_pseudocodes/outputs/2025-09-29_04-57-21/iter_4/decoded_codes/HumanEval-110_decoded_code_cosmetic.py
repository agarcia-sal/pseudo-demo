from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0
    idx_one: int = 0
    while idx_one < len(list_one):
        current_val = list_one[idx_one]
        remainder = current_val - 2 * (current_val // 2)
        if remainder == 1:
            tally_odd += 1
        idx_one += 1

    idx_two: int = 0
    while idx_two < len(list_two):
        val_at_two = list_two[idx_two]
        if not (val_at_two - 2 * (val_at_two // 2) == 1):
            tally_even += 1
        idx_two += 1

    if not (tally_even < tally_odd):
        return "YES"
    return "NO"