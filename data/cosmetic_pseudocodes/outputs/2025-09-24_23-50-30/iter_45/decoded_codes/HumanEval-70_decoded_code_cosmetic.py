from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    accumulated_sequence: List[int] = []
    toggle_switch: int = 1
    while list_of_integers:
        candidate_value = min(list_of_integers) if toggle_switch != 0 else max(list_of_integers)
        accumulated_sequence.append(candidate_value)
        list_of_integers.remove(candidate_value)
        toggle_switch = 1 - toggle_switch
    return accumulated_sequence