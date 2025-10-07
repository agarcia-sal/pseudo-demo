from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    acc_odd: int = 0
    acc_even: int = 0
    idx_one: int = 0
    while idx_one < len(list_one):
        if list_one[idx_one] % 2 != 0:
            acc_odd += 1
        idx_one += 1

    idx_two: int = 0
    while idx_two < len(list_two):
        if list_two[idx_two] % 2 == 0:
            acc_even += 1
        idx_two += 1

    if acc_even >= acc_odd:
        return "YES"
    else:
        return "NO"