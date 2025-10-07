from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier = -1
        digits_list = [int(ch) for ch in str(integer_value)]
        digits_list[0] *= multiplier
        return sum(digits_list)

    digit_sums: List[int] = [digits_sum(number) for number in array_of_integers]
    positive_sums = [value for value in digit_sums if value > 0]
    return len(positive_sums)