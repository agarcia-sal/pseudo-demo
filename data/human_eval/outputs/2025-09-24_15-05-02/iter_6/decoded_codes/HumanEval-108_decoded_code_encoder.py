from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(number: int) -> int:
        sign = 1
        if number < 0:
            number = -number
            sign = -1
        digits_list = [int(ch) for ch in str(number)]
        digits_list[0] *= sign
        return sum(digits_list)

    digit_sums = [digits_sum(element) for element in array_of_integers]
    filtered_list = [value for value in digit_sums if value > 0]
    return len(filtered_list)