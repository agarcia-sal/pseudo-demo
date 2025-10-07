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

    digit_sums = []
    for element in array_of_integers:
        digit_sums.append(digits_sum(element))

    positive_sums = [x for x in digit_sums if x > 0]
    return len(positive_sums)