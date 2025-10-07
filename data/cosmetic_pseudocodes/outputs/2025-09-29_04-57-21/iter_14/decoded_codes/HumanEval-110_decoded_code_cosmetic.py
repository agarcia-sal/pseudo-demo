from typing import List, Union

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    index_a: int = 0
    while index_a < len(list_one):
        current_num: int = list_one[index_a]
        if current_num % 2 != 0:
            tally_odd += 1
        index_a += 1

    index_b: int = 0
    while index_b < len(list_two):
        if list_two[index_b] % 2 == 0:
            tally_even += 1
        index_b += 1

    if not (tally_even < tally_odd):
        return "YES"

    return "NO"