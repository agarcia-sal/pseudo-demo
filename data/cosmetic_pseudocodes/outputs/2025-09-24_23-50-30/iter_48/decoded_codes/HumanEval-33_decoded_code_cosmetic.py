from typing import Sequence, TypeVar, List

T = TypeVar('T')

def sort_third(container_param: Sequence[T]) -> List[T]:
    buffer_list: List[T] = []
    iterator_num: int = 0
    length = len(container_param)
    while iterator_num < length:
        if (iterator_num % 3) == 0:
            buffer_list.append(container_param[iterator_num])
        iterator_num += 1

    cursor_idx: int = 0
    # Perform selection sort directly on buffer_list
    while cursor_idx < len(buffer_list):
        current_min = buffer_list[cursor_idx]
        scan_idx = cursor_idx + 1
        while scan_idx < len(buffer_list):
            if buffer_list[scan_idx] < current_min:
                # Swap values to reflect new minimum
                current_min = buffer_list[scan_idx]
                buffer_list[scan_idx] = buffer_list[cursor_idx]
                buffer_list[cursor_idx] = current_min
            scan_idx += 1
        cursor_idx += 1

    result_list: List[T] = []
    pos_idx: int = 0
    replace_idx: int = 0
    while pos_idx < length:
        if (pos_idx % 3) == 0:
            result_list.append(buffer_list[replace_idx])
            replace_idx += 1
        else:
            result_list.append(container_param[pos_idx])
        pos_idx += 1

    return result_list