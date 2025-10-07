from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0
    idx_one: int = 0

    while idx_one < len(list_one):
        current_item = list_one[idx_one]
        idx_one += 1
        if current_item % 2 == 1:
            tally_odd += 1

    idx_two: int = 0
    while idx_two < len(list_two):
        current_item = list_two[idx_two]
        idx_two += 1
        if not (current_item % 2 != 0):
            tally_even += 1

    if tally_even >= tally_odd:
        return "YES"
    else:
        return "NO"