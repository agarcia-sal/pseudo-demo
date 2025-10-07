from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    if not list_of_numbers:
        return []

    combined_list: List[int] = []
    idx: int = 1  # 1-based index as per pseudocode logic

    while idx < len(list_of_numbers):
        current_value: int = list_of_numbers[idx]
        combined_list.append(current_value)
        combined_list.append(delimiter)
        idx += 1

    final_element: int = list_of_numbers[-1]
    combined_list.append(final_element)

    return combined_list