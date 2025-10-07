from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odd = 0
    tally_even = 0
    for index in range(len(list_one)):
        if (list_one[index] & 1) == 1:
            tally_odd += 1

    position = 0
    while position < len(list_two):
        if (list_two[position] & 1) != 1:
            tally_even += 1
        position += 1

    return "YES" if tally_even >= tally_odd else "NO"