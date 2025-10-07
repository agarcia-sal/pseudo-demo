from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output: List[int] = []
    toggle: bool = True
    integers = list_of_integers[:]  # Make a copy to avoid mutating input
    while integers:
        chosen_value = min(integers) if toggle else max(integers)
        output.append(chosen_value)
        integers.remove(chosen_value)
        toggle = not toggle
    return output