from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    count_odd: int = 0
    count_even: int = 0

    index_odd: int = 0
    while index_odd < len(list_one):
        val_odd: int = list_one[index_odd]
        if (val_odd + 1) % 2 != 0:
            count_odd += 1
        index_odd += 1

    index_even: int = 0
    while index_even < len(list_two):
        val_even: int = list_two[index_even]
        if val_even % 2 == 0:
            count_even += 1
        index_even += 1

    if count_even >= count_odd:
        return "YES"
    else:
        return "NO"