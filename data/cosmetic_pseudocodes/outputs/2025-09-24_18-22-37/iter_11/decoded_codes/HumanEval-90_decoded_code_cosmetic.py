from typing import List, Optional

def next_smallest(array_integers: List[int]) -> Optional[int]:
    trimmed_array: List[int] = []
    index_counter: int = 0
    element_found: bool = False  # variable declared but unused as per pseudocode

    while index_counter < len(array_integers):
        current_element: int = array_integers[index_counter]

        is_duplicate: bool = False
        for checked_element in trimmed_array:
            if checked_element == current_element:
                is_duplicate = True
                break

        if not is_duplicate:
            trimmed_array.append(current_element)

        index_counter += 1

    trimmed_array.sort()

    length_trimmed: int = len(trimmed_array)

    if length_trimmed < 2:
        return_value: Optional[int] = None
    else:
        return_value = trimmed_array[1]

    return return_value