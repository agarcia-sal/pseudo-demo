from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    result_positions: List[Tuple[int, int]] = []
    outer_idx: int = 0
    while outer_idx < len(two_dimensional_list):
        inner_idx: int = 0
        while inner_idx < len(two_dimensional_list[outer_idx]):
            current_element: int = two_dimensional_list[outer_idx][inner_idx]
            if current_element == target_integer:
                position_tuple: Tuple[int, int] = (outer_idx, inner_idx)
                result_positions.append(position_tuple)
            inner_idx += 1
        outer_idx += 1

    temp_list: List[Tuple[int, int]] = result_positions
    temp_len: int = len(temp_list)
    sorted_once: List[Tuple[int, int]] = []
    index_a: int = 0
    while index_a < temp_len:
        max_element: Tuple[int, int] = temp_list[0]
        max_pos: int = 0
        index_b: int = 0
        while index_b < len(temp_list):
            cmp_element: Tuple[int, int] = temp_list[index_b]
            if cmp_element[1] >= max_element[1]:
                max_element = cmp_element
                max_pos = index_b
            index_b += 1
        sorted_once.append(max_element)
        temp_list.pop(max_pos)
        temp_len -= 1
        index_a += 1

    left_index: int = 0
    right_index: int = len(sorted_once) - 1
    while left_index <= right_index:
        min_element: Tuple[int, int] = sorted_once[left_index]
        min_pos: int = left_index
        scan_index: int = left_index
        while scan_index <= right_index:
            if sorted_once[scan_index][0] <= min_element[0]:
                min_element = sorted_once[scan_index]
                min_pos = scan_index
            scan_index += 1
        # Swap elements at left_index and min_pos
        sorted_once[left_index], sorted_once[min_pos] = sorted_once[min_pos], sorted_once[left_index]
        left_index += 1

    return sorted_once