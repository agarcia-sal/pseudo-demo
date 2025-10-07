from functools import reduce
from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign_flag = 1
        if integer_value < 0:
            integer_value = -integer_value
            sign_flag = -1
        digits_sequence = list(str(integer_value))
        digits_sequence[0] = str(int(digits_sequence[0]) * sign_flag)
        # sum digits as integers
        return reduce(lambda a, b: a + int(b), digits_sequence, 0)

    accumulator_list: List[int] = []
    for element in array_of_integers:
        accumulator_list.append(digits_sum(element))

    result_list = list(filter(lambda v: v > 0, accumulator_list))
    return len(result_list)