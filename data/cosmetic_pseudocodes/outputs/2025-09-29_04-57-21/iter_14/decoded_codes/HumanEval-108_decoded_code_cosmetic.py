from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        polarity = 1
        if integer_value < 0:
            integer_value = -integer_value
            polarity = -1
        digits_str = str(integer_value)
        digits_array: List[int] = [int(ch) for ch in digits_str]
        digits_array[0] *= polarity
        total_sum = sum(digits_array)
        return total_sum

    sums_collection: List[int] = [digits_sum(value) for value in array_of_integers]
    count_positive = sum(1 for s in sums_collection if s > 0)
    return count_positive