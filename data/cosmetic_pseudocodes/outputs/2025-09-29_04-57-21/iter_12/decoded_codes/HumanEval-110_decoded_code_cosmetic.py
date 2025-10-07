from typing import List


def exchange(list_one: List[int], list_two: List[int]) -> str:
    total_odd = 0
    total_even = 0

    idx = 0
    while idx < len(list_one):
        current_num = list_one[idx]
        if current_num % 2 != 0:
            total_odd += 1
        idx += 1

    pos = 0
    while pos < len(list_two):
        value = list_two[pos]
        if not (value % 2 != 0):
            total_even += 1
        pos += 1

    if total_odd > total_even:
        return "NO"
    else:
        return "YES"