from typing import List, Sequence


def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    acc_one: int = 0
    acc_two: int = 0
    idx_one: int = 0
    while idx_one < len(list_one):
        item_one: str = list_one[idx_one]
        acc_one += len(item_one)
        idx_one += 1
    idx_two: int = 0
    while idx_two < len(list_two):
        item_two: str = list_two[idx_two]
        acc_two += len(item_two)
        idx_two += 1
    if not (acc_one > acc_two):
        return list_one
    return list_two