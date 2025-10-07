from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        if integer_value >= 0:
            absolute_value = integer_value
            multiplier = 1
        else:
            absolute_value = -integer_value
            multiplier = -1

        digits_list = [int(char) for char in str(absolute_value)]
        digits_list[0] *= multiplier

        total = sum(digits_list)
        return total

    sums_collection = [digits_sum(item) for item in array_of_integers]
    positive_sums = [value for value in sums_collection if value > 0]

    return len(positive_sums)