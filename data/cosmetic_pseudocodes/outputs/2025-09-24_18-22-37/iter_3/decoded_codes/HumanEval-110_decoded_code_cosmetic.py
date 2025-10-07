from typing import List, Literal

def exchange(list_one: List[int], list_two: List[int]) -> Literal["YES", "NO"]:
    odd_total: int = 0
    index_a: int = 0
    while index_a < len(list_one):
        val_a = list_one[index_a]
        if val_a % 2 != 0:
            odd_total += 1
        index_a += 1

    even_total: int = 0
    index_b: int = 0
    while index_b < len(list_two):
        val_b = list_two[index_b]
        if val_b % 2 == 0:
            even_total += 1
        index_b += 1

    if even_total >= odd_total:
        return "YES"
    else:
        return "NO"