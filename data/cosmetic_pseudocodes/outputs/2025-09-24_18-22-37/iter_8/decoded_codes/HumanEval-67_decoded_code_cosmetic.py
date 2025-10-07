from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    number_collection: List[int] = []
    element_index: int = 0
    elements_list: List[str] = string_description.split(' ')
    while element_index < len(elements_list):
        current_string: str = elements_list[element_index]
        element_index += 1
        if current_string.isdigit():
            temp_number: int = int(current_string)
            number_collection.append(temp_number)
    total_accumulated: int = 0
    idx: int = 0
    while idx < len(number_collection):
        value_at_idx: int = number_collection[idx]
        total_accumulated += value_at_idx
        idx += 1
    return total_number_of_fruits - total_accumulated