from functools import reduce
from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        flag_sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            flag_sign = -1
        chars_list = str(integer_value)
        digit_values = [int(c) for c in chars_list]
        digit_values[0] *= flag_sign
        return reduce(lambda acc, val: acc + val, digit_values, 0)

    def gather_sums(init_index: int, limit_index: int, input_arr: List[int], acc_arr: List[int]) -> List[int]:
        if not (init_index < limit_index):
            return acc_arr
        updated_acc = acc_arr + [digits_sum(input_arr[init_index])]
        return gather_sums(init_index + 1, limit_index, input_arr, updated_acc)

    all_sums = gather_sums(0, len(array_of_integers), array_of_integers, [])
    positive_sums = [val for val in all_sums if val > 0]
    return len(positive_sums)