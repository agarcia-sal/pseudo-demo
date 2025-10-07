from typing import List, TypeVar

T = TypeVar('T')


def sort_third(list_input: List[T]) -> List[T]:
    temp_list: List[T] = list(list_input)
    extracted_values: List[T] = [temp_list[idx] for idx in range(len(temp_list)) if idx % 3 == 0]
    ordered_values: List[T] = sorted(extracted_values)
    pos: int = 0
    for index in range(len(temp_list)):
        if index % 3 == 0:
            temp_list[index] = ordered_values[pos]
            pos += 1
    return temp_list