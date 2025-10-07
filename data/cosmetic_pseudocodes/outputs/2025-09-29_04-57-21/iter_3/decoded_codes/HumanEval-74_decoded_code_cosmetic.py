from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_lengths_one: int = sum(len(current_str) for current_str in list_one)
    sum_lengths_two: int = sum(len(current_str) for current_str in list_two)
    if not (sum_lengths_one > sum_lengths_two):
        return list_one
    return list_two