from typing import List


def order_by_points(list_of_numbers: List[int]) -> List[int]:
    def digits_sum(number: int) -> int:
        polarity_flag = 1
        while number < 0:
            number = -number
            polarity_flag = -1
        split_digits = [int(ch) for ch in str(number)]
        split_digits[0] *= polarity_flag
        input_sum = sum(split_digits)
        return input_sum

    return sorted(list_of_numbers, key=digits_sum)