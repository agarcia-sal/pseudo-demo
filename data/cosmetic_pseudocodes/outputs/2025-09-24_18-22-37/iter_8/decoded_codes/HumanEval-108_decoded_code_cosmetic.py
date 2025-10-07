from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign_flipper = 1
        if integer_value < 0:
            integer_value = -integer_value
            sign_flipper = -1

        integer_as_string = str(integer_value)
        array_of_characters = list(integer_as_string)
        list_of_digits: List[int] = []
        idx_counter = 0
        while idx_counter < len(array_of_characters):
            current_char = array_of_characters[idx_counter]
            current_digit = int(current_char)
            list_of_digits.append(current_digit)
            idx_counter += 1

        first_digit = list_of_digits[0]
        adjusted_first_digit = first_digit * sign_flipper
        list_of_digits[0] = adjusted_first_digit

        accumulator = 0
        accumulator += list_of_digits[0]
        idx_iterator = 1
        while idx_iterator < len(list_of_digits):
            accumulator += list_of_digits[idx_iterator]
            idx_iterator += 1

        return accumulator

    temp_sums_list: List[int] = []
    arr_idx = 0
    while arr_idx < len(array_of_integers):
        element = array_of_integers[arr_idx]
        digit_sum_result = digits_sum(element)
        temp_sums_list.append(digit_sum_result)
        arr_idx += 1

    positive_elements: List[int] = []
    temp_idx = 0
    while temp_idx < len(temp_sums_list):
        candidate = temp_sums_list[temp_idx]
        if candidate > 0:
            positive_elements.append(candidate)
        temp_idx += 1

    return len(positive_elements)