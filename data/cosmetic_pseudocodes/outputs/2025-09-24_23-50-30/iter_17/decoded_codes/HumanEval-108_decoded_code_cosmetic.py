from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        if integer_value >= 0:
            sign_flag = 1
            abs_val = integer_value
        else:
            sign_flag = -1
            abs_val = -integer_value

        digits_str = str(abs_val)
        digit_values: List[int] = [int(d) for d in digits_str]
        digit_values[0] *= sign_flag

        total_sum = sum(digit_values)
        return total_sum

    intermediate_results: List[int] = []
    idx = 0
    while idx < len(array_of_integers):
        intermediate_results.append(digits_sum(array_of_integers[idx]))
        idx += 1

    count_positive = 0
    iter_pos = 0
    while iter_pos < len(intermediate_results):
        if intermediate_results[iter_pos] > 0:
            count_positive += 1
        iter_pos += 1

    return count_positive