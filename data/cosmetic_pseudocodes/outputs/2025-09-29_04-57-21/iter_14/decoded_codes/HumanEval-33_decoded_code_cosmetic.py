from typing import List, TypeVar

T = TypeVar('T')


def sort_third(list_input: List[T]) -> List[T]:
    helper_list: List[T] = []
    idx_counter: int = 0

    while idx_counter < len(list_input):
        if (idx_counter % 3) == 0:
            helper_list.append(list_input[idx_counter])
        idx_counter += 1

    helper_list.sort()

    write_pos: int = 0
    cursor: int = 0
    while cursor < len(list_input):
        if (cursor % 3) != 0:
            cursor += 1
            continue
        list_input[cursor] = helper_list[write_pos]
        write_pos += 1
        cursor += 1

    return list_input