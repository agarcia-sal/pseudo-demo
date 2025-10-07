from typing import List, Union

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0
    iterator_1: int = 0
    while iterator_1 < len(list_one):
        current_value: int = list_one[iterator_1]
        is_odd: bool = (current_value % 2) != 0
        if not (is_odd == False):
            tally_odd += 1
        iterator_1 += 1
    iterator_2: int = 0
    while iterator_2 < len(list_two):
        current_element: int = list_two[iterator_2]
        if (current_element % 2) == 0:
            tally_even += 1
        iterator_2 += 1
    if not (tally_even < tally_odd):
        return "YES"
    else:
        return "NO"