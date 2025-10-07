from typing import List, Sequence

def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    sum_one = 0
    index_a = 0
    while index_a < len(list_one):
        sum_one += len(list_one[index_a])
        index_a += 1

    sum_b = 0
    idx_b = 0
    while idx_b < len(list_two):
        sum_b += len(list_two[idx_b])
        idx_b += 1

    if not (sum_b < sum_one):
        return list_one
    return list_two