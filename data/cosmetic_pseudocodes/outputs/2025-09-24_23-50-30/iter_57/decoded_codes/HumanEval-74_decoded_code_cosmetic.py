from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    acc_one: int = 0
    idx_one: int = 0
    while idx_one < len(list_one):
        current_str_one = list_one[idx_one]
        acc_one += len(current_str_one)
        idx_one += 1

    acc_two: int = 0
    idx_two: int = 0
    while True:
        if idx_two >= len(list_two):
            break
        current_str_two = list_two[idx_two]
        acc_two += len(current_str_two)
        idx_two += 1

    if acc_one > acc_two:
        return list_two
    else:
        return list_one