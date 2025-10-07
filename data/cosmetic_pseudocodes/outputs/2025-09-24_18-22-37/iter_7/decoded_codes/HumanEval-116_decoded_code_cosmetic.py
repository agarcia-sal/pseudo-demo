from typing import List


def sort_array(list_of_numbers: List[int]) -> List[int]:
    intermediate_list: List[int] = list_of_numbers[:]
    temporary_list: List[int] = intermediate_list

    index_i: int = 0
    while index_i < len(intermediate_list):
        index_j: int = index_i + 1
        while index_j < len(intermediate_list):
            if temporary_list[index_i] > temporary_list[index_j]:
                temporary_list[index_i], temporary_list[index_j] = (
                    temporary_list[index_j],
                    temporary_list[index_i],
                )
            index_j += 1
        index_i += 1

    sorted_array_based_on_decimal: List[int] = temporary_list
    length_of_sorted: int = len(sorted_array_based_on_decimal)
    position_x: int = 0
    while position_x < length_of_sorted:
        position_y: int = position_x + 1
        while position_y < length_of_sorted:
            binary_x: str = bin(sorted_array_based_on_decimal[position_x])
            count_ones_x: int = 0
            char_index_x: int = 2
            while char_index_x < len(binary_x):
                if binary_x[char_index_x] == "1":
                    count_ones_x += 1
                char_index_x += 1

            binary_y: str = bin(sorted_array_based_on_decimal[position_y])
            count_ones_y: int = 0
            char_index_y: int = 2
            while char_index_y < len(binary_y):
                if binary_y[char_index_y] == "1":
                    count_ones_y += 1
                char_index_y += 1

            if count_ones_x > count_ones_y:
                sorted_array_based_on_decimal[position_x], sorted_array_based_on_decimal[position_y] = (
                    sorted_array_based_on_decimal[position_y],
                    sorted_array_based_on_decimal[position_x],
                )
            position_y += 1
        position_x += 1

    final_sorted_array: List[int] = sorted_array_based_on_decimal
    return final_sorted_array