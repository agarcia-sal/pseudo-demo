from typing import List, Union

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    iterator_one: int = 0
    while iterator_one < len(list_one):
        current_value: int = list_one[iterator_one]
        if current_value % 2 != 0:
            tally_odd += 1
        iterator_one += 1

    index_two: int = 0
    while index_two < len(list_two):
        item: int = list_two[index_two]
        if item % 2 == 0:
            tally_even += 1
        index_two += 1

    if not (tally_even < tally_odd):
        return "YES"
    return "NO"