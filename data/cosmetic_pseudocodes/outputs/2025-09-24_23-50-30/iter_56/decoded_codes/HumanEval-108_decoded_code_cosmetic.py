from functools import reduce
from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign_flag: int = -1
        adjusted_number: int = integer_value
        if integer_value >= 0:
            sign_flag = 1
        else:
            adjusted_number = -integer_value
        digits_array: List[int] = [int(ch) for ch in str(adjusted_number)]
        digits_array[0] *= sign_flag
        return reduce(lambda acc, val: acc + val, digits_array, 0)

    def accumulate_sums(index: int, collection: List[int], accumulator: List[int]) -> List[int]:
        if index >= len(collection):
            return accumulator
        return accumulate_sums(index + 1, collection, accumulator + [digits_sum(collection[index])])

    digit_sums: List[int] = accumulate_sums(0, array_of_integers, [])

    def filter_positive_items(source_list: List[int], position: int, collected: List[int]) -> List[int]:
        if position >= len(source_list):
            return collected
        new_collected = collected + ([source_list[position]] if source_list[position] > 0 else [])
        return filter_positive_items(source_list, position + 1, new_collected)

    positive_items: List[int] = filter_positive_items(digit_sums, 0, [])

    return len(positive_items)