from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    temp_list: List[T] = list_input.copy()
    collected_elements: List[T] = []
    idx: int = 0
    while idx < len(temp_list):
        if idx % 3 == 0:
            collected_elements.append(temp_list[idx])
        idx += 1

    collected_elements.sort()

    write_pos: int = 0
    write_index: int = 0
    while write_pos < len(temp_list):
        if write_pos % 3 == 0:
            temp_list[write_pos] = collected_elements[write_index]
            write_index += 1
        write_pos += 1

    return temp_list