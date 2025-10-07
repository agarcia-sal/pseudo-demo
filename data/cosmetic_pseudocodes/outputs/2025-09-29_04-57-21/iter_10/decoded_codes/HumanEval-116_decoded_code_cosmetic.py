from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    ascending_ordered_list = array_of_integers[:]
    index_counter = 0

    # Bubble sort for initial ascending order
    while index_counter < len(ascending_ordered_list) - 1:
        current_index = 0
        while current_index < len(ascending_ordered_list) - index_counter - 1:
            if ascending_ordered_list[current_index] > ascending_ordered_list[current_index + 1]:
                # swap elements
                ascending_ordered_list[current_index], ascending_ordered_list[current_index + 1] = (
                    ascending_ordered_list[current_index + 1], ascending_ordered_list[current_index]
                )
            current_index += 1
        index_counter += 1

    def binary_ones_counter(number: int) -> int:
        count_ones = 0
        binary_string = bin(number)
        char_index = 0
        while char_index < len(binary_string):
            if binary_string[char_index] == "1":
                count_ones += 1
            char_index += 1
        return count_ones

    def compare_by_ones(a: int, b: int) -> int:
        a_ones = binary_ones_counter(a)
        b_ones = binary_ones_counter(b)
        if a_ones < b_ones:
            return -1
        elif a_ones > b_ones:
            return 1
        else:
            return 0

    n = len(ascending_ordered_list)
    i = 1

    # Insertion sort by number of ones in binary representation, then by value
    while i < n:
        key_element = ascending_ordered_list[i]
        j = i - 1
        key_ones = binary_ones_counter(key_element)
        while (
            j >= 0
            and (
                binary_ones_counter(ascending_ordered_list[j]) > key_ones
                or (
                    binary_ones_counter(ascending_ordered_list[j]) == key_ones
                    and ascending_ordered_list[j] > key_element
                )
            )
        ):
            ascending_ordered_list[j + 1] = ascending_ordered_list[j]
            j -= 1
        ascending_ordered_list[j + 1] = key_element
        i += 1

    return ascending_ordered_list