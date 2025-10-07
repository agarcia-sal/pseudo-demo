from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    aggregate_length_a: int = 0
    aggregate_length_b: int = 0

    idx_a: int = 0
    while idx_a < len(list_one):
        aggregate_length_a += len(list_one[idx_a])
        idx_a += 1

    idx_b: int = 0
    while idx_b < len(list_two):
        aggregate_length_b += len(list_two[idx_b])
        idx_b += 1

    if aggregate_length_a <= aggregate_length_b:
        return list_one
    else:
        return list_two