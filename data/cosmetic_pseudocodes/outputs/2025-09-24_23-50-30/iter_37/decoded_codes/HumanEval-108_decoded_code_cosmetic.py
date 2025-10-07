from functools import reduce
from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier_sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier_sign = -1
        chars_list = list(str(integer_value))
        digits_list = [int(ch) for ch in chars_list]
        if multiplier_sign == -1:
            digits_list[0] *= multiplier_sign
        total = reduce(lambda x, y: x + y, digits_list, 0)
        return total

    sums_collection: List[int] = []
    index = 0
    while index < len(array_of_integers):
        sums_collection.append(digits_sum(array_of_integers[index]))
        index += 1

    positive_sums = [value for value in sums_collection if value > 0]

    return len(positive_sums)