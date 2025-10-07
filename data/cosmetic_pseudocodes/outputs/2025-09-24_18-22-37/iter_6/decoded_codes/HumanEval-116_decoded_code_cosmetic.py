from typing import List


def sort_array(original_list: List[int]) -> List[int]:
    intermediate_sorted_list: List[int] = original_list[:]
    index_counter: int = 0

    # Insertion sort portion
    while index_counter < len(original_list):
        current_value: int = original_list[index_counter]
        position: int = 0
        while position < index_counter and intermediate_sorted_list[position] <= current_value:
            position += 1
        shift_index: int = index_counter
        while shift_index > position:
            intermediate_sorted_list[shift_index] = intermediate_sorted_list[shift_index - 1]
            shift_index -= 1
        intermediate_sorted_list[position] = current_value
        index_counter += 1

    length_of_list: int = len(intermediate_sorted_list)
    outer_index: int = 0

    # Custom sorting based on count of '1's in binary representation, starting from 4th bit
    while outer_index < length_of_list:
        inner_index: int = outer_index + 1
        while inner_index < length_of_list:
            first_value: int = intermediate_sorted_list[outer_index]
            second_value: int = intermediate_sorted_list[inner_index]

            # Convert to binary strings
            first_binary_str: str = bin(first_value)
            second_binary_str: str = bin(second_value)

            count_ones_first: int = 0
            count_ones_second: int = 0

            # Count '1's starting from the 4th bit (index 3), if string is long enough
            char_index_first: int = 0
            while char_index_first < len(first_binary_str) - 3:
                if first_binary_str[char_index_first + 3] == '1':
                    count_ones_first += 1
                char_index_first += 1

            char_index_second: int = 0
            while char_index_second < len(second_binary_str) - 3:
                if second_binary_str[char_index_second + 3] == '1':
                    count_ones_second += 1
                char_index_second += 1

            if count_ones_first > count_ones_second:
                intermediate_sorted_list[outer_index], intermediate_sorted_list[inner_index] = (
                    intermediate_sorted_list[inner_index],
                    intermediate_sorted_list[outer_index],
                )
            inner_index += 1
        outer_index += 1

    return intermediate_sorted_list