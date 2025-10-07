from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        if integer_value < 0:
            abs_val = abs(integer_value)
            first_digit = -int(str(abs_val)[0])
            rest_digits = [int(ch) for ch in str(abs_val)[1:]]
            return first_digit + sum(rest_digits)
        else:
            digits = [int(ch) for ch in str(integer_value)]
            return sum(digits)

    results: List[int] = [digits_sum(num) for num in array_of_integers]
    positive_counts = sum(1 for val in results if val > 0)
    return positive_counts