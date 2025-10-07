from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odds: int = 0
    tally_evens: int = 0
    iterator_one: int = 0
    while iterator_one < len(list_one):
        current_val: int = list_one[iterator_one]
        if current_val % 2 != 0:
            tally_odds += 1
        iterator_one += 1
    iterator_two: int = 0
    while iterator_two < len(list_two):
        current_val = list_two[iterator_two]
        if current_val % 2 == 0:
            tally_evens += 1
        iterator_two += 1
    if not (tally_evens < tally_odds):
        return "YES"
    else:
        return "NO"