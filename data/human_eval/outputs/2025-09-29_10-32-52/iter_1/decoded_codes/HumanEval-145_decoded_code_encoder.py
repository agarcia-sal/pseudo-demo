from typing import List

def order_by_points(list_of_numbers: List[int]) -> List[int]:
    def digits_sum(number: int) -> int:
        sign_indicator = 1
        if number < 0:
            number = -number
            sign_indicator = -1
        digits_list = [int(d) for d in str(number)]
        if digits_list:
            digits_list[0] *= sign_indicator
        return sum(digits_list)
    return sorted(list_of_numbers, key=digits_sum)