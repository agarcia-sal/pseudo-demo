from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        if integer_value >= 0:
            abs_value = integer_value
            first_digit_multiplier = 1
        else:
            abs_value = -integer_value
            first_digit_multiplier = -1
        chars = list(str(abs_value))
        digits_list = [int(char) for char in chars]
        digits_list[0] *= first_digit_multiplier
        total_sum = sum(digits_list)
        return total_sum

    temp_results: List[int] = [digits_sum(num) for num in array_of_integers]
    positive_items = [val for val in temp_results if val > 0]
    return len(positive_items)