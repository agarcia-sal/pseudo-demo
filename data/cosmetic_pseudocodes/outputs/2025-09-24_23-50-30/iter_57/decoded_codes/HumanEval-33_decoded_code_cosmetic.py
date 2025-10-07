from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    list_copy: List[T] = list_input.copy()
    selected_elements: List[T] = []
    index: int = 0

    while index < len(list_copy):
        if index % 3 == 0:
            selected_elements.append(list_copy[index])
        index += 1

    sorted_selected: List[T] = sorted(selected_elements)

    write_index: int = 0
    read_index: int = 0

    while read_index < len(list_copy):
        if not (read_index % 3 != 0):
            list_copy[read_index] = sorted_selected[write_index]
            write_index += 1
        read_index += 1

    return list_copy