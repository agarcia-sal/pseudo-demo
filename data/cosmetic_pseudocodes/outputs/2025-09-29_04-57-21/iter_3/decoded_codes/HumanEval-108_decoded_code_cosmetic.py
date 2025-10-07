from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        polarity = 1
        if integer_value < 0:
            integer_value = -integer_value
            polarity = -1

        digit_values = [int(ch) for ch in str(integer_value)]
        digit_values[0] *= polarity

        return sum(digit_values)

    calculated_sums: List[int] = [digits_sum(num) for num in array_of_integers]
    result_list: List[int] = [val for val in calculated_sums if val > 0]

    return len(result_list)