from typing import List


def order_by_points(list_of_numbers: List[int]) -> List[int]:
    def digits_sum(number: int) -> int:
        sign_indicator = -1 if number < 0 else 1
        number = abs(number)
        digits_array: List[int] = []
        while number > 0:
            digits_array.append(number % 10)
            number //= 10
        if not digits_array:
            digits_array.append(0)
        digits_array[-1] *= sign_indicator  # apply sign to the last digit
        return sum(digits_array)

    return sorted(list_of_numbers, key=digits_sum)