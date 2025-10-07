from functools import reduce
from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        if integer_value < 0:
            integer_value = -integer_value
            first_digit_sign = -1
        else:
            first_digit_sign = 1
        str_digits = str(integer_value)
        digit_values = [int(ch) for ch in str_digits]
        digit_values[0] *= first_digit_sign
        return reduce(lambda a, b: a + b, digit_values)

    return len([x for x in (digits_sum(n) for n in array_of_integers) if x > 0])