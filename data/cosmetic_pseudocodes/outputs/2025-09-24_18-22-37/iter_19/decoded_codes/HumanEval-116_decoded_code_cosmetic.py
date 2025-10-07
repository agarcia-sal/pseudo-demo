from typing import List, Tuple


def sort_array(array_of_integers: List[int]) -> List[int]:
    temp_sorted_decimals: List[int] = array_of_integers[:]

    # Bubble sort temp_sorted_decimals ascending
    while True:
        swapped_flag = False
        for index_i in range(1, len(temp_sorted_decimals)):
            if temp_sorted_decimals[index_i - 1] > temp_sorted_decimals[index_i]:
                temp_sorted_decimals[index_i - 1], temp_sorted_decimals[index_i] = (
                    temp_sorted_decimals[index_i],
                    temp_sorted_decimals[index_i - 1],
                )
                swapped_flag = True
        if not swapped_flag:
            break

    temp_map: List[Tuple[int, int]] = []

    # Count ones in binary representation from 3rd character onward ('0b' prefix included, so skip '0b')
    for element_counter in temp_sorted_decimals:
        binary_form = bin(element_counter)
        count_ones = sum(1 for ch in binary_form[2:] if ch == "1")
        temp_map.append((element_counter, count_ones))

    # Bubble sort temp_map by count_ones ascending, then element_counter ascending
    while True:
        swapped_flag = False
        for index_i in range(1, len(temp_map)):
            prev_elem, prev_count = temp_map[index_i - 1]
            curr_elem, curr_count = temp_map[index_i]

            if prev_count > curr_count or (
                prev_count == curr_count and prev_elem > curr_elem
            ):
                temp_map[index_i - 1], temp_map[index_i] = temp_map[index_i], temp_map[index_i - 1]
                swapped_flag = True
        if not swapped_flag:
            break

    result_array: List[int] = [elem for elem, _ in temp_map]
    return result_array