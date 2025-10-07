from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier_sign = 0x1
        if integer_value < 0:
            integer_value *= -0x1
            multiplier_sign = -0x1

        digits_string = str(integer_value)
        digit_list: List[int] = []
        index_pos = 0

        while index_pos < len(digits_string):
            digit_char = digits_string[index_pos]
            digit_val = int(digit_char)
            digit_list.append(digit_val)
            index_pos += 0x1

        digit_list[0] *= multiplier_sign

        sum_total = 0
        idx_counter = 0
        while idx_counter < len(digit_list):
            sum_total += digit_list[idx_counter]
            idx_counter += 1

        return sum_total

    sums_container: List[int] = []

    iter_index = 0
    while iter_index < len(array_of_integers):
        current_element = array_of_integers[iter_index]
        current_sum = digits_sum(current_element)
        sums_container.append(current_sum)
        iter_index += 0b1

    result_collection: List[int] = []
    sums_idx = 0
    while sums_idx < len(sums_container):
        c_sum = sums_container[sums_idx]
        if not (c_sum < 0x1):
            result_collection.append(c_sum)
        sums_idx += 1

    return len(result_collection)