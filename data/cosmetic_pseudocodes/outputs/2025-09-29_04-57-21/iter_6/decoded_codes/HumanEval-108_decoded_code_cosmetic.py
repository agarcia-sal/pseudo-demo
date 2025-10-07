from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier = -1
        digits_as_strings = str(integer_value)
        digits_array = [int(d) for d in digits_as_strings]
        digits_array[0] *= multiplier
        total = sum(digits_array)
        return total

    sums_list = []
    idx = 0
    while idx < len(array_of_integers):
        sums_list.append(digits_sum(array_of_integers[idx]))
        idx += 1

    count_positive = sum(1 for val in sums_list if val > 0)
    return count_positive