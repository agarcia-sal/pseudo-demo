from typing import List


def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    aggregate_one = 0
    idx = 0
    while idx < len(list_one):
        aggregate_one += len(list_one[idx])
        idx += 1

    aggregate_two = 0
    cursor = 0
    while cursor < len(list_two):
        aggregate_two += len(list_two[cursor])
        cursor += 1

    if not (aggregate_two < aggregate_one):
        return list_one
    return list_two