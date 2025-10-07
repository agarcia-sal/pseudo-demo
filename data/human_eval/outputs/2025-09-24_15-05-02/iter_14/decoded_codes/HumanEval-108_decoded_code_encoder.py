from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(number: int) -> int:
        sign = 1
        if number < 0:
            number = -number
            sign = -1
        digits = list(map(int, str(number)))
        digits[0] = digits[0] * sign
        total_sum = sum(digits)
        return total_sum

    digit_sums = []
    for element in array_of_integers:
        digit_sums.append(digits_sum(element))
    filtered_list = [item for item in digit_sums if item > 0]
    result = len(filtered_list)
    return result