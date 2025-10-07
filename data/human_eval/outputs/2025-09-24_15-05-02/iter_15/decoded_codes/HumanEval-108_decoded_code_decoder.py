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
    list_of_sums = [digits_sum(num) for num in array_of_integers]
    filtered = [s for s in list_of_sums if s > 0]
    return len(filtered)