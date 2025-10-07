from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        if integer_value >= 0:
            normalized_value = integer_value
            multiplier = 1
        else:
            normalized_value = -integer_value
            multiplier = -1

        digits_array = [int(d) for d in str(normalized_value)]
        digits_array[0] *= multiplier

        sum_result = sum(digits_array)
        return sum_result

    collected_sums: List[int] = []
    idx = 0
    while idx < len(array_of_integers):
        collected_sums.append(digits_sum(array_of_integers[idx]))
        idx += 1

    positive_values: List[int] = [value for value in collected_sums if value > 0]

    return len(positive_values)