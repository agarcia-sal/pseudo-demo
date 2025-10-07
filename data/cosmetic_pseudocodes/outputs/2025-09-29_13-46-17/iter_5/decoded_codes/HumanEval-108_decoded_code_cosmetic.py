from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        negation_flag = 1
        # Normalize negative integer_value to positive, but flip negation_flag once if negative
        while integer_value < 0:
            integer_value = -integer_value
            negation_flag = -1

        digits_str_arr = str(integer_value)
        digits_nums: List[int] = []
        idx_camel = 0
        while idx_camel < len(digits_str_arr):
            digits_nums.append(int(digits_str_arr[idx_camel]))
            idx_camel += 1

        digits_nums[0] = digits_nums[0] * negation_flag

        total_acc = 0
        iterator_go = 0
        while iterator_go < len(digits_nums):
            total_acc += digits_nums[iterator_go]
            iterator_go += 1

        return total_acc

    acc_list_: List[int] = []
    ix_index_0 = 0
    while ix_index_0 < len(array_of_integers):
        acc_list_.append(digits_sum(array_of_integers[ix_index_0]))
        ix_index_0 += 1

    def predicate_pos(x_parameter: int) -> bool:
        return not (x_parameter <= 0)

    unfiltered_ = acc_list_
    filtered_: List[int] = []
    pos_i = 0
    while pos_i < len(unfiltered_):
        if predicate_pos(unfiltered_[pos_i]):
            filtered_.append(unfiltered_[pos_i])
        pos_i += 1

    return len(filtered_)