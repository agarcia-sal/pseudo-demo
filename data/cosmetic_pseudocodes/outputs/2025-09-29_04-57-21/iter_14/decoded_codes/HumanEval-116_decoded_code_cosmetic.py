from typing import List


def quick_sort_asc(list_to_sort: List[int]) -> None:
    if len(list_to_sort) <= 1:
        return
    pivot_element = list_to_sort[0]
    lesser_values: List[int] = []
    greater_values: List[int] = []
    scan_index = 1
    while scan_index < len(list_to_sort):
        if list_to_sort[scan_index] < pivot_element:
            lesser_values.append(list_to_sort[scan_index])
        else:
            greater_values.append(list_to_sort[scan_index])
        scan_index += 1
    quick_sort_asc(lesser_values)
    quick_sort_asc(greater_values)
    list_to_sort[:] = lesser_values + [pivot_element] + greater_values


def sort_array(array_of_integers: List[int]) -> List[int]:
    intermediate_result: List[int] = []
    index_pointer = 0
    while index_pointer < len(array_of_integers):
        intermediate_result.append(array_of_integers[index_pointer])
        index_pointer += 1

    quick_sort_asc(intermediate_result)

    processed_list: List[List[int]] = []
    for item in intermediate_result:
        binary_chars: str = bin(item)
        count_ones = 0
        char_pos = 2  # Skip '0b' prefix of binary string
        while char_pos < len(binary_chars):
            if binary_chars[char_pos] == '1':
                count_ones += 1
            char_pos += 1
        processed_list.append([item, count_ones])

    sorted_by_ones: List[int] = []
    while len(processed_list) > 0:
        current_min = processed_list[0]
        min_index = 0
        scan_index = 1
        while scan_index < len(processed_list):
            if (processed_list[scan_index][1] < current_min[1] or
                (processed_list[scan_index][1] == current_min[1] and processed_list[scan_index][0] < current_min[0])):
                current_min = processed_list[scan_index]
                min_index = scan_index
            scan_index += 1
        sorted_by_ones.append(current_min[0])
        processed_list.pop(min_index)

    return sorted_by_ones