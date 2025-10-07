from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    list_copy: List[T] = [item for item in list_input]

    selected_elements: List[T] = [list_copy[i] for i in range(len(list_copy)) if i % 3 == 0]

    sorted_selection: List[T] = sorted(selected_elements)

    write_pos = 0
    for read_pos in range(len(list_copy)):
        if read_pos % 3 == 0:
            list_copy[read_pos] = sorted_selection[write_pos]
            write_pos += 1

    return list_copy