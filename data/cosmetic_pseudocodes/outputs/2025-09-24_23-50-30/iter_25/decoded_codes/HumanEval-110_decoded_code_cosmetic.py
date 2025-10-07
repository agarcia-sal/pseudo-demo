from typing import List, Union

def exchange(list_one: List[int], list_two: List[int]) -> str:
    count_odd: int = 0
    count_even: int = 0
    index_a: int = 0
    while index_a < len(list_one):
        if list_one[index_a] % 2 != 0:
            count_odd += 1
        index_a += 1

    index_b: int = 0
    while index_b < len(list_two):
        if list_two[index_b] % 2 == 0:
            count_even += 1
        index_b += 1

    if not (count_even < count_odd):
        return "YES"
    else:
        return "NO"