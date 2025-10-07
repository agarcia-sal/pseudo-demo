from functools import reduce
from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier_sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier_sign = -1
        digits_list = [int(char) for char in str(integer_value)]
        digits_list[0] *= multiplier_sign
        return reduce(lambda acc, val: acc + val, digits_list, 0)

    sums_collection: List[int] = []
    iterator_elements = iter(array_of_integers)
    while True:
        try:
            current_val = next(iterator_elements)
        except StopIteration:
            break
        sums_collection.append(digits_sum(current_val))

    positive_sums = [item for item in sums_collection if item > 0]

    return len(positive_sums)