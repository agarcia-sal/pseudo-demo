from typing import List

def rescale_to_unit(numbers_list: List[float]) -> List[float]:
    small_val = numbers_list[0]
    large_val = numbers_list[0]

    for each_element in numbers_list:
        if each_element < small_val:
            small_val = each_element
        elif each_element > large_val:
            large_val = each_element

    range_val = large_val - small_val
    scaled_list: List[float] = []
    index_counter = 0

    while index_counter < len(numbers_list):
        current_val = numbers_list[index_counter]
        adjusted_val = (current_val - small_val) / range_val
        scaled_list.append(adjusted_val)
        index_counter += 1

    return scaled_list