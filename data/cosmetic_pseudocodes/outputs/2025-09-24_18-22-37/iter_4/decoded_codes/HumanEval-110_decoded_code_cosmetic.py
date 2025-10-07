from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    odd_counter: int = 0
    even_counter: int = 0

    idx1: int = 0
    while idx1 < len(list_one):
        val: int = list_one[idx1]
        if val % 2 == 1:
            odd_counter += 1
        idx1 += 1

    idx2: int = 0
    while idx2 < len(list_two):
        val2: int = list_two[idx2]
        if val2 % 2 == 0:
            even_counter += 1
        idx2 += 1

    if even_counter >= odd_counter:
        return "YES"
    else:
        return "NO"