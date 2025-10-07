from functools import reduce
from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        delta_sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            delta_sign = -1
        digit_chunks = [int(d) for d in str(integer_value)]
        digit_chunks[0] *= delta_sign
        return reduce(lambda acc, val: acc + val, digit_chunks, 0)

    accumulator_list: List[int] = []
    for element in array_of_integers:
        accumulator_list.append(digits_sum(element))

    return len([element for element in accumulator_list if element > 0])