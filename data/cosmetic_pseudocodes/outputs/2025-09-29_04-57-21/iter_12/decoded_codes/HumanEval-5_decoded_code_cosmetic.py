from typing import List, Union

def intersperse(list_of_numbers: List[Union[int, float]], delimiter: Union[int, float]) -> List[Union[int, float]]:
    if not list_of_numbers:
        return []
    assembled_list: List[Union[int, float]] = []
    current_index = 0
    while current_index < len(list_of_numbers) - 1:
        current_value = list_of_numbers[current_index]
        assembled_list.append(current_value)
        assembled_list.append(delimiter)
        current_index += 1
    final_element = list_of_numbers[-1]
    assembled_list.append(final_element)
    return assembled_list