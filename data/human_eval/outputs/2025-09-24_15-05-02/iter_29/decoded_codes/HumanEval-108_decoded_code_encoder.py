from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_number: int) -> int:
        sign_multiplier = 1
        if integer_number < 0:
            integer_number = -integer_number
            sign_multiplier = -1
        list_of_digits = [int(d) for d in str(integer_number)]
        list_of_digits[0] *= sign_multiplier
        total_sum = sum(list_of_digits)
        return total_sum

    list_of_digit_sums = [digits_sum(element) for element in array_of_integers]
    filtered_list = [x for x in list_of_digit_sums if x > 0]
    count_positive_sums = len(filtered_list)
    return count_positive_sums