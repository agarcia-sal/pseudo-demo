from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier_sign: int = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier_sign = -1

        string_digits: str = str(integer_value)
        digit_list: List[int] = [int(string_digits[i]) for i in range(len(string_digits))]

        digit_list[0] *= multiplier_sign  # first digit multiplied by sign

        total: int = sum(digit_list)
        return total

    sum_digits_list: List[int] = []
    idx: int = 0
    while idx < len(array_of_integers):
        sum_digits_list.append(digits_sum(array_of_integers[idx]))
        idx += 1

    positive_list: List[int] = [val for val in sum_digits_list if val > 0]

    return len(positive_list)