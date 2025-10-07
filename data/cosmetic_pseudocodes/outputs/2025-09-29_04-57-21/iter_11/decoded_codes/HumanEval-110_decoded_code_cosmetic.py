from typing import List, Union

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    index_one: int = 0
    while index_one < len(list_one):
        val: int = list_one[index_one]
        if (val % 2) == 1:
            tally_odd += 1
        index_one += 1

    cursor_two: int = 0
    while cursor_two < len(list_two):
        item: int = list_two[cursor_two]
        if not ((item % 2) != 0):  # item is even
            tally_even += 1
        cursor_two += 1

    if not (tally_even < tally_odd):
        return "YES"
    return "NO"