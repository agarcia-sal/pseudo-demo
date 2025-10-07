from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    working_copy: List[T] = list_input[:]
    extracted_values: List[T] = []

    position: int = 0
    while position < len(working_copy):
        if position % 3 == 0:
            extracted_values.append(working_copy[position])
        position += 1

    ordered_values: List[T] = sorted(extracted_values)

    insert_pos: int = 0
    current_index: int = 0
    while current_index < len(working_copy):
        if current_index % 3 == 0:
            working_copy[current_index] = ordered_values[insert_pos]
            insert_pos += 1
        current_index += 1

    return working_copy