from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(number: int) -> int:
        sign = 1
        if number < 0:
            number = -number
            sign = -1
        digits = [int(d) for d in str(number)]
        digits[0] *= sign
        return sum(digits)

    digit_sums = [digits_sum(num) for num in array_of_integers]
    filtered_digit_sums = [s for s in digit_sums if s > 0]
    count = len(filtered_digit_sums)
    return count