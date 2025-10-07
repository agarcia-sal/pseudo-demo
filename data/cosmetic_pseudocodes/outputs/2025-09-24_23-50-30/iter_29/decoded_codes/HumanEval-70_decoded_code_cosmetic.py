from typing import List

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_flag: bool = True
    numbers = array_of_numbers.copy()  # avoid mutating input list

    while numbers:
        if not toggle_flag:
            chosen_element = max(numbers)
        else:
            chosen_element = min(numbers)
        output_sequence.append(chosen_element)
        numbers.remove(chosen_element)
        toggle_flag = not toggle_flag

    return output_sequence