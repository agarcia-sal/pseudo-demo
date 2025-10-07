from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign_factor = 1
        if integer_value < 0:
            integer_value = -integer_value
            sign_factor = -1
        str_digits = str(integer_value)
        digit_list = [int(char_digit) for char_digit in str_digits]
        digit_list[0] *= sign_factor
        total_sum = sum(digit_list)
        return total_sum

    sums_collection: List[int] = []
    for current_element in array_of_integers:
        sum_value = digits_sum(current_element)
        sums_collection.append(sum_value)

    filtered_sums = [candidate for candidate in sums_collection if candidate > 0]

    return len(filtered_sums)