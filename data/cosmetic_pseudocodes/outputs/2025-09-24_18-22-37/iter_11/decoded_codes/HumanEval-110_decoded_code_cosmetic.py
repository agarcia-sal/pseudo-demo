from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    total_odd: int = 0
    total_even: int = 0

    idx_a: int = 0
    while idx_a < len(list_one):
        current_val_a: int = list_one[idx_a]
        remainder_a: int = current_val_a % 2
        if remainder_a == 1:
            total_odd += 1
        idx_a += 1

    idx_b: int = 0
    while idx_b < len(list_two):
        current_val_b: int = list_two[idx_b]
        remainder_b: int = current_val_b % 2
        if remainder_b == 0:
            total_even += 1
        idx_b += 1

    comparison_result: bool = total_even >= total_odd
    if comparison_result:
        return "YES"
    else:
        return "NO"