from typing import List, Tuple


def sort_array(input_list: List[int]) -> List[int]:
    temp_ordered_list: List[int] = []
    index_counter: int = 0
    while index_counter < len(input_list):
        temp_ordered_list.append(input_list[index_counter])
        index_counter += 1

    temp_ordered_list.sort()

    result_list: List[Tuple[int, int]] = []
    ptr: int = 0
    while ptr < len(temp_ordered_list):
        current_element: int = temp_ordered_list[ptr]
        binary_str: str = bin(current_element)[2:]  # convert to binary without '0b'
        count_ones: int = 0
        char_index: int = 3
        while char_index < len(binary_str):
            if binary_str[char_index] == '1':
                count_ones += 1
            char_index += 1
        result_list.append((current_element, count_ones))
        ptr += 1

    sorted_results: List[Tuple[int, int]] = []
    n: int = len(result_list)
    p: int = 0
    while p < n:
        q: int = p + 1
        while q < n:
            first_elem = result_list[p]
            second_elem = result_list[q]
            if (first_elem[1] > second_elem[1]) or (
                (first_elem[1] == second_elem[1]) and (first_elem[0] > second_elem[0])
            ):
                result_list[p], result_list[q] = second_elem, first_elem
            q += 1
        p += 1

    output_array: List[int] = []
    for pair in result_list:
        output_array.append(pair[0])

    return output_array