from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(number: int) -> int:
        sign = 1
        if number < 0:
            number = -number
            sign = -1
        digit_list = [int(d) for d in str(number)]
        if digit_list:
            digit_list[0] *= sign
        return sum(digit_list)

    digit_sums: List[int] = [digits_sum(element) for element in array_of_integers]
    filtered_list: List[int] = [value for value in digit_sums if value > 0]
    return len(filtered_list)