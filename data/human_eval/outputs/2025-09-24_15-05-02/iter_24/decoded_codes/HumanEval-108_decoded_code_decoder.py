from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(number: int) -> int:
        sign = 1
        if number < 0:
            number = -number
            sign = -1
        digits = [int(d) for d in str(number)]
        if digits:
            digits[0] *= sign  # Apply sign only to the first digit
        return sum(digits)

    list_of_sums = [digits_sum(element) for element in array_of_integers]
    positive_sums = [val for val in list_of_sums if val > 0]
    return len(positive_sums)