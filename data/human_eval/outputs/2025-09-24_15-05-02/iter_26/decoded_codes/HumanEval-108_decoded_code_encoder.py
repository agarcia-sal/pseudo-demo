from typing import List

def count_nums(list_of_integers: List[int]) -> int:
    def digits_sum(integer_number: int) -> int:
        sign = 1
        if integer_number < 0:
            integer_number = -integer_number
            sign = -1
        digits: List[int] = [int(d) for d in str(integer_number)]
        digits[0] *= sign
        return sum(digits)

    list_of_sums: List[int] = [digits_sum(number) for number in list_of_integers]
    filtered_list: List[int] = [digit_sum for digit_sum in list_of_sums if digit_sum > 0]

    return len(filtered_list)