from typing import List

def sort_third(array_param: List[int]) -> List[int]:
    buffer: List[int] = []
    current_index: int = 0
    while current_index < len(array_param):
        if current_index % 3 == 0:
            buffer.append(array_param[current_index])
        current_index += 1

    insertion_index: int = 0
    while insertion_index < len(buffer):
        min_value = buffer[insertion_index]
        swap_pos = insertion_index
        pos = insertion_index + 1
        while pos < len(buffer):
            if buffer[pos] < min_value:
                min_value = buffer[pos]
                swap_pos = pos
            pos += 1
        if min_value != buffer[insertion_index]:
            buffer[insertion_index], buffer[swap_pos] = buffer[swap_pos], buffer[insertion_index]
        insertion_index += 1

    index_array = 0
    index_buffer = 0
    while index_array < len(array_param):
        if index_array % 3 == 0:
            array_param[index_array] = buffer[index_buffer]
            index_buffer += 1
        index_array += 1

    return array_param