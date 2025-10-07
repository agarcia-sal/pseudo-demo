from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        multiplier_sign: int = 1
        if integer_value < 0:
            integer_value = -integer_value
            multiplier_sign = -1

        digits_str: str = str(integer_value)
        digit_list: List[int] = [int(ch) for ch in digits_str]
        digit_list[0] *= multiplier_sign

        total_sum: int = sum(digit_list)
        return total_sum

    accumulated_sums: List[int] = [digits_sum(num) for num in array_of_integers]
    positives_only: List[int] = [val for val in accumulated_sums if val > 0]

    return len(positives_only)