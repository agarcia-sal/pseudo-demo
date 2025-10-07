from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    accumulator: List[int] = []
    toggle: int = 1
    while list_of_integers:
        chosen_element = min(list_of_integers) if toggle == 1 else max(list_of_integers)
        accumulator.append(chosen_element)
        # Remove only the last occurrence of chosen_element
        last_index = len(list_of_integers) - 1 - list_of_integers[::-1].index(chosen_element)
        list_of_integers = [
            x for i, x in enumerate(list_of_integers)
            if x != chosen_element or i != last_index
        ]
        toggle = -toggle
    return accumulator