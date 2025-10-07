from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier_sign = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier_sign = -multiplier_sign
        digits_list = [int(char) for char in str(integer_value)]
        digits_list[0] *= multiplier_sign
        total_sum = sum(digits_list)
        return total_sum

    results_accumulator: List[int] = []
    idx = 0
    while idx < len(array_of_integers):
        current_element = array_of_integers[idx]
        results_accumulator.append(digits_sum(current_element))
        idx += 1

    positive_values = [val for val in results_accumulator if val > 0]

    return len(positive_values)