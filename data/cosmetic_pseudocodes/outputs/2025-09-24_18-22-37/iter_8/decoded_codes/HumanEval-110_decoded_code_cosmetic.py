from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0

    iterator_a: int = 0
    while iterator_a < len(list_one):
        item_a: int = list_one[iterator_a]
        if item_a % 2 == 1:
            tally_odd += 1
        iterator_a += 1

    iterator_b: int = 0
    while iterator_b < len(list_two):
        item_b: int = list_two[iterator_b]
        if item_b % 2 == 0:
            tally_even += 1
        iterator_b += 1

    if tally_even >= tally_odd:
        return "YES"
    else:
        return "NO"