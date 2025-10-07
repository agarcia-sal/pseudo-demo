from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        negation_factor = 1
        if integer_value < 0:
            integer_value = -integer_value
            negation_factor = -1
        list_of_signed_digits = [int(d) for d in str(integer_value)]
        list_of_signed_digits[0] *= negation_factor
        return sum(list_of_signed_digits)

    list_of_digit_sums: List[int] = [digits_sum(integer_element) for integer_element in array_of_integers]
    filtered_list = [elem for elem in list_of_digit_sums if elem > 0]
    return len(filtered_list)