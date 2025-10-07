from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    accumulator: List[int] = []
    toggle: int = 1
    while list_of_integers:
        if toggle == 1:
            pick = min(list_of_integers)
        else:
            pick = max(list_of_integers)
        accumulator.append(pick)
        # Remove all occurrences of pick
        list_of_integers = [x for x in list_of_integers if x != pick]
        toggle = -toggle
    return accumulator