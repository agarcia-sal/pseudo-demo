from functools import reduce
from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier_sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier_sign = -1

        digits_list = [int(c) for c in str(integer_value)]
        digits_list[0] *= multiplier_sign

        return reduce(lambda acc, val: acc + val, digits_list, 0)

    digit_sums_list = list(map(digits_sum, array_of_integers))
    positive_filtered: List[int] = []

    for val in digit_sums_list:
        if val <= 0:
            continue
        positive_filtered.append(val)

    return len(positive_filtered)