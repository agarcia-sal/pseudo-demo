from typing import List, TypeVar

T = TypeVar('T')

def sort_third(received_array: List[T]) -> List[T]:
    buffer_list: List[T] = list(received_array)
    gathered_elements: List[T] = []
    pos_counter: int = 0

    while pos_counter < len(buffer_list):
        gathered_elements.append(buffer_list[pos_counter])
        pos_counter += 3

    sorted_collection: List[T] = sorted(gathered_elements)

    write_index: int = 0
    replace_position: int = 0

    while replace_position < len(buffer_list):
        buffer_list[replace_position] = sorted_collection[write_index]
        write_index += 1
        replace_position += 3

    return buffer_list