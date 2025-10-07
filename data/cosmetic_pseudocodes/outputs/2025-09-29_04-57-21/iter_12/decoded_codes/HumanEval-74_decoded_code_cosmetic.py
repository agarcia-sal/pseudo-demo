from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_chars_one: int = 0
    idx_one: int = 0
    while idx_one < len(list_one):
        current_str: str = list_one[idx_one]
        sum_chars_one += len(current_str)
        idx_one += 1

    sum_chars_two: int = 0
    position_two: int = 0
    while position_two < len(list_two):
        candidate_str: str = list_two[position_two]
        sum_chars_two += len(candidate_str)
        position_two += 1

    if not (sum_chars_one > sum_chars_two):
        return list_one
    return list_two