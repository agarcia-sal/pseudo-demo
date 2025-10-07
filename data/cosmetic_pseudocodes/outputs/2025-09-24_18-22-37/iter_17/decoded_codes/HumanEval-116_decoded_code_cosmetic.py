from typing import List

def sort_array(list_of_ints: List[int]) -> List[int]:
    temp_list1: List[int] = []
    iterator_var: int = 0
    while iterator_var < len(list_of_ints):
        temp_list1.append(list_of_ints[iterator_var])
        iterator_var += 1

    temp_list1.sort()
    temp_list2: List[int] = []
    iterator_idx: int = 0
    while iterator_idx < len(temp_list1):
        temp_list2.append(temp_list1[iterator_idx])
        iterator_idx += 1

    def count_ones_after_first_two_bits(curr_val: int) -> int:
        bin_rep = bin(curr_val)  # binary string with '0b' prefix
        count_ones = 0
        str_index = 2  # start after '0b'
        while str_index < len(bin_rep):
            if bin_rep[str_index] == '1':
                count_ones += 1
            str_index += 1
        return count_ones

    result_list = sorted(temp_list2, key=count_ones_after_first_two_bits)
    return result_list