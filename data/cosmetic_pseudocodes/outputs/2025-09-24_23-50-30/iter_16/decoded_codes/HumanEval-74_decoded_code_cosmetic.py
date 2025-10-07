from typing import List, Sequence

def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    acc_one: int = 0
    acc_two: int = 0
    idx_one: int = 0
    while idx_one < len(list_one):
        acc_one += len(list_one[idx_one])
        idx_one += 1

    idx_two: int = 0
    while idx_two < len(list_two):
        acc_two += len(list_two[idx_two])
        idx_two += 1

    return list_one if acc_one <= acc_two else list_two