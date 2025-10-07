from typing import List


def order_by_points(list_of_numbers: List[int]) -> List[int]:
    def digits_sum(number: int) -> int:
        multiplier = 1
        if number < 0:
            number = -number
            multiplier = -1
        digits_collection = [int(d) for d in str(number)]
        digits_collection[0] *= multiplier
        return sum(digits_collection)

    return sorted(list_of_numbers, key=digits_sum)