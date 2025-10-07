from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    temp_list: List[T] = list(list_input)
    extracted_values: List[T] = []
    idx: int = 0
    while idx < len(temp_list):
        if idx % 3 == 0:
            extracted_values.append(temp_list[idx])
        idx += 1
    sorted_extracted: List[T] = sorted(extracted_values)
    insertion_index: int = 0
    position: int = 0
    while position < len(temp_list):
        if position % 3 == 0:
            temp_list[position] = sorted_extracted[insertion_index]
            insertion_index += 1
        position += 1
    return temp_list