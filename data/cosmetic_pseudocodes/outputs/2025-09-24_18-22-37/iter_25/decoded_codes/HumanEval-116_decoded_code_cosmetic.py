from typing import List


def sort_array(sequence_of_numbers: List[int]) -> List[int]:
    intermediate_ordered_list: List[int] = sequence_of_numbers.copy()

    # Sort numerically in ascending order
    n = len(intermediate_ordered_list)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if intermediate_ordered_list[i] > intermediate_ordered_list[j]:
                intermediate_ordered_list[i], intermediate_ordered_list[j] = intermediate_ordered_list[j], intermediate_ordered_list[i]

    # Sort based on count of '1's in binary form, preserving previous order on ties
    for p in range(n - 1):
        for q in range(p + 1, n):
            current_element = intermediate_ordered_list[q]
            temporary_binary_string = bin(current_element)
            bit_count = sum(1 for ch in temporary_binary_string[2:] if ch == '1')

            current_element = intermediate_ordered_list[p]
            temporary_binary_string = bin(current_element)
            previous_bit_count = sum(1 for ch in temporary_binary_string[2:] if ch == '1')

            if bit_count < previous_bit_count:
                intermediate_ordered_list[p], intermediate_ordered_list[q] = intermediate_ordered_list[q], intermediate_ordered_list[p]

    binary_ones_keyed_list: List[int] = intermediate_ordered_list
    return binary_ones_keyed_list