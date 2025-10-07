from functools import reduce
from typing import List

def count_nums(collection_of_values: List[int]) -> int:
    def digits_sum(number_value: int) -> int:
        multiplier_sign: int = 1
        if number_value < 0:
            number_value = -number_value
            multiplier_sign = -1
        character_digits: List[str] = list(str(number_value))
        integer_digits: List[int] = [int(c) for c in character_digits]
        integer_digits[0] *= multiplier_sign
        return reduce(lambda a, b: a + b, integer_digits)

    def accumulate_sums(values: List[int], index: int, accumulator: List[int]) -> List[int]:
        if index >= len(values):
            return accumulator
        return accumulate_sums(values, index + 1, accumulator + [digits_sum(values[index])])

    sums_list: List[int] = accumulate_sums(collection_of_values, 0, [])

    def filter_positive(lst: List[int], idx: int, res: List[int]) -> List[int]:
        if idx == len(lst):
            return res
        if lst[idx] > 0:
            return filter_positive(lst, idx + 1, res + [lst[idx]])
        return filter_positive(lst, idx + 1, res)

    positives: List[int] = filter_positive(sums_list, 0, [])
    return len(positives)