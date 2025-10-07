from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle: int = 1
    remaining = list_of_integers.copy()
    while remaining:
        candidate = min(remaining) if toggle == 1 else max(remaining)
        output_sequence.append(candidate)
        remaining.remove(candidate)
        toggle = -toggle
    return output_sequence