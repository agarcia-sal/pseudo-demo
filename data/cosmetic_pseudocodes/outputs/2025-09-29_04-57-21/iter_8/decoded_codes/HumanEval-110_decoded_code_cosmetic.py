from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odd = 0
    tally_even = 0

    iterator_one = 0
    while iterator_one < len(list_one):
        current_item = list_one[iterator_one]
        is_odd = ((current_item + 1) % 2) != 0  # True if current_item is odd
        if is_odd:
            tally_odd += 1
        iterator_one += 1

    iterator_two = 0
    while True:
        if iterator_two >= len(list_two):
            break
        current_unit = list_two[iterator_two]
        if (current_unit % 2) == 0:
            tally_even += 1
        iterator_two += 1

    if not (tally_even < tally_odd):
        return "YES"

    return "NO"