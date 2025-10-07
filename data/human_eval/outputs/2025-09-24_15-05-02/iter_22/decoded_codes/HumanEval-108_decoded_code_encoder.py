from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(number: int) -> int:
        sign_multiplier = 1
        if number < 0:
            number = -number
            sign_multiplier = -1
        digit_list = [int(char) for char in str(number)]
        # Apply sign to the first digit only
        digit_list[0] *= sign_multiplier
        return sum(digit_list)

    positive_sum_count = 0
    for element in array_of_integers:
        current_sum = digits_sum(element)
        if current_sum > 0:
            positive_sum_count += 1
    return positive_sum_count