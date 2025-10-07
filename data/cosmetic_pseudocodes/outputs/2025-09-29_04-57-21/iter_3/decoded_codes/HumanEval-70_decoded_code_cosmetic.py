from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    final_sequence: List[int] = []
    pick_minimum: bool = True

    # Work on a copy to avoid modifying the original list
    integers = list_of_integers.copy()

    while integers:
        if pick_minimum:
            chosen_value = min(integers)
        else:
            chosen_value = max(integers)

        final_sequence.append(chosen_value)
        integers.remove(chosen_value)
        pick_minimum = not pick_minimum

    return final_sequence