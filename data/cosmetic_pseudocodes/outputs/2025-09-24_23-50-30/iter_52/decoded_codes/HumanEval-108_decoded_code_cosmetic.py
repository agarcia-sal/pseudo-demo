from functools import reduce
from typing import List, Sequence


def count_nums(collection_of_ints: Sequence[int]) -> int:
    def digits_sum(value_int: int) -> int:
        factor_sign = 1
        if value_int < 0:
            value_int = -value_int
            factor_sign = -1
        digit_seq = [int(char) for char in str(value_int)]
        digit_seq[0] *= factor_sign
        return reduce(lambda a, b: a + b, digit_seq, 0)

    def build_sums(input_sequence: Sequence[int], acc_list: List[int]) -> List[int]:
        if not input_sequence:
            return acc_list
        return build_sums(input_sequence[1:], acc_list + [digits_sum(input_sequence[0])])

    sums_collection = build_sums(collection_of_ints, [])
    positive_collection = filter(lambda n: n > 0, sums_collection)
    return len(list(positive_collection))