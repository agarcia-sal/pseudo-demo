from typing import List, Sequence

def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    idx_a: int = 0
    total_a: int = 0
    while idx_a < len(list_one):
        total_a += len(list_one[idx_a])
        idx_a += 1

    pos_b: int = 0
    total_b: int = 0
    while pos_b < len(list_two):
        total_b += len(list_two[pos_b])
        pos_b += 1

    if total_a <= total_b:
        return list_one
    else:
        return list_two