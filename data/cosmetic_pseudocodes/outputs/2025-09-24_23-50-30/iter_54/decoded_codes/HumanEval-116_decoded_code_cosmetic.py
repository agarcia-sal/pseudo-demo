from typing import List

def sort_array(input_list: List[int]) -> List[int]:
    temp_list = input_list.copy()
    temp_list.sort()  # Sort numbers in ascending natural order

    def count_ones(binary_str: str) -> int:
        index = 0
        ones_counter = 0
        while index < len(binary_str):
            if binary_str[index] == '1':
                ones_counter += 1
            index += 1
        return ones_counter

    def ones_key(number: int) -> int:
        bin_str = bin(number)
        # Remove '0b' prefix and the last character (equivalent to substring from 2 to len-2)
        binary_repr = bin_str[2:-1] if len(bin_str) > 3 else ''
        return count_ones(binary_repr)

    index_pointer = 1
    while index_pointer < len(temp_list):
        current_value = temp_list[index_pointer]
        current_key = ones_key(current_value)
        inner_index = index_pointer - 1
        while inner_index >= 0 and ones_key(temp_list[inner_index]) > current_key:
            temp_list[inner_index + 1] = temp_list[inner_index]
            inner_index -= 1
        temp_list[inner_index + 1] = current_value
        index_pointer += 1

    return temp_list