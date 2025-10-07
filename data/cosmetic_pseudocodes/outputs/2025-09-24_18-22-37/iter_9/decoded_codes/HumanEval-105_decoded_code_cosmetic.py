from typing import List

def by_length(inputs_list: List[int]) -> List[str]:
    number_name_map = {
        0x1: "One",
        0x2: "Two",
        0x3: "Three",
        0x4: "Four",
        0x5: "Five",
        0x6: "Six",
        0x7: "Seven",
        0x8: "Eight",
        0x9: "Nine",
    }
    temp_list = inputs_list[:]
    descending_sorted: List[int] = []

    while temp_list:
        max_value = temp_list[0]
        idx = 1
        while idx < len(temp_list):
            if temp_list[idx] > max_value:
                max_value = temp_list[idx]
            idx += 1
        descending_sorted.append(max_value)
        temp_list.remove(max_value)

    result_list: List[str] = []
    index_counter = 0
    while index_counter < len(descending_sorted):
        current_element = descending_sorted[index_counter]
        if current_element in number_name_map:
            result_list.append(number_name_map[current_element])
        index_counter += 1

    return result_list