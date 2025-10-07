from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        polarity_factor = 1
        if integer_value < 0:
            integer_value = -integer_value
            polarity_factor = -polarity_factor
        digit_chars = str(integer_value)
        digits_list: List[int] = [int(ch) for ch in digit_chars]
        digits_list[0] *= polarity_factor
        total_sum = sum(digits_list)
        return total_sum

    digit_sums_collection: List[int] = [digits_sum(val) for val in array_of_integers]
    filtered_collection = [item for item in digit_sums_collection if item > 0]
    return len(filtered_collection)