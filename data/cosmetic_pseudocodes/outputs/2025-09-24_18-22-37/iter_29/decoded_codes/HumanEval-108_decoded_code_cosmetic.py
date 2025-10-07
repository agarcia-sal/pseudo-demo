from typing import Sequence


def count_nums(collection_of_values: Sequence[int]) -> int:
    def digits_sum(num_val: int) -> int:
        multiplier_sign = 1
        if num_val < 0:
            num_val = -num_val
            multiplier_sign = -1
        digits_str = str(num_val)
        digits_array = [int(ch) for ch in digits_str]
        digits_array[0] *= multiplier_sign  # apply sign only to the most significant digit
        total_sum = sum(digits_array)
        return total_sum

    result_values = [digits_sum(val_b) for val_b in collection_of_values]
    positive_results = [candidate for candidate in result_values if candidate > 0]
    return len(positive_results)