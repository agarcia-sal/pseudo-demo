from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    sorted_output: List[int] = []
    pick_minimum: int = 1
    while len(list_of_integers) > 0:
        if pick_minimum == 0:
            chosen_element = max(list_of_integers)
        else:
            chosen_element = min(list_of_integers)

        sorted_output.append(chosen_element)

        # Remove the first occurrence of chosen_element
        for index_position, value in enumerate(list_of_integers):
            if value == chosen_element:
                del list_of_integers[index_position]
                break

        pick_minimum = 1 - pick_minimum

    return sorted_output