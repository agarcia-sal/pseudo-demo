from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier_sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier_sign = -1

        string_representation = str(integer_value)
        digit_list: List[int] = []
        index_counter = 0
        while index_counter < len(string_representation):
            char_element = string_representation[index_counter]
            numeric_digit = int(char_element)
            digit_list.append(numeric_digit)
            index_counter += 1

        digit_list[0] = digit_list[0] * multiplier_sign

        sum_accumulator = 0
        sum_index = 0
        while sum_index < len(digit_list):
            sum_accumulator += digit_list[sum_index]
            sum_index += 1

        return sum_accumulator

    digit_sums_list: List[int] = []
    iteration_index = 0
    while iteration_index < len(array_of_integers):
        current_element = array_of_integers[iteration_index]
        computed_sum = digits_sum(current_element)
        digit_sums_list.append(computed_sum)
        iteration_index += 1

    filtered_positive_list: List[int] = []
    filter_index = 0
    while filter_index < len(digit_sums_list):
        current_value = digit_sums_list[filter_index]
        if current_value > 0:
            filtered_positive_list.append(current_value)
        filter_index += 1

    result = len(filtered_positive_list)
    return result