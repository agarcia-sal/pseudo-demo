from typing import List

def COUNT_ONES(number_input: int) -> int:
    binary_str = bin(number_input)[2:]  # binary representation without '0b'
    sum_ones = 0
    pos_counter = 0
    length = len(binary_str)
    while pos_counter < length:
        if binary_str[pos_counter] == '1':
            sum_ones += 1
        pos_counter += 1
    return sum_ones

def sort_array(array_input: List[int]) -> List[int]:
    intermediate_sorted_list: List[int] = []
    idx_counter = 0
    length = len(array_input)
    while idx_counter < length:
        intermediate_sorted_list.append(array_input[idx_counter])
        idx_counter += 1

    index_var = 1
    limit_var = len(intermediate_sorted_list)
    while index_var < limit_var:
        current_val = intermediate_sorted_list[index_var]
        bitstr = bin(current_val)[2:]
        ones_total = 0
        char_index = 0
        bit_length = len(bitstr)
        while char_index < bit_length:
            if bitstr[char_index] == '1':
                ones_total += 1
            char_index += 1

        insert_pos = index_var - 1
        while insert_pos >= 0 and (
            ones_total < COUNT_ONES(intermediate_sorted_list[insert_pos]) or
            (ones_total == COUNT_ONES(intermediate_sorted_list[insert_pos]) and current_val < intermediate_sorted_list[insert_pos])
        ):
            intermediate_sorted_list[insert_pos + 1] = intermediate_sorted_list[insert_pos]
            insert_pos -= 1
        intermediate_sorted_list[insert_pos + 1] = current_val
        index_var += 1

    return intermediate_sorted_list