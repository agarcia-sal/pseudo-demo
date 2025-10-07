from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    count_odd: int = 0
    count_even: int = 0

    idx: int = 0
    while idx < len(list_one):
        if list_one[idx] % 2 != 0:
            count_odd += 1
        idx += 1

    pos: int = 0
    while pos < len(list_two):
        if list_two[pos] % 2 == 0:
            count_even += 1
        pos += 1

    if count_odd > count_even:
        return "NO"
    else:
        return "YES"