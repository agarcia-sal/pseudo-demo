from typing import List


def order_by_points(list_of_numbers: List[int]) -> List[int]:
    def digits_sum(number: int) -> int:
        polarity = 1
        if number < 0:
            number = -number
            polarity = -1
        digits_array = [int(d) for d in str(number)]
        digits_array[0] *= polarity
        return sum(digits_array)

    return sorted(list_of_numbers, key=digits_sum)