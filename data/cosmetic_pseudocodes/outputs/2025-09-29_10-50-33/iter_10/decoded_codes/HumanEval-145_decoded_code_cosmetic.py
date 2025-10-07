from functools import reduce
from typing import List


def order_by_points(list_of_numbers: List[int]) -> List[int]:
    def digits_sum(number: int) -> int:
        polarity = 1
        if number < 0:
            number = -number
            polarity = -1
        digits_sequence = [int(char) for char in str(number)]
        digits_sequence[0] *= polarity
        return reduce(lambda acc, elem: acc + elem, digits_sequence, 0)

    return sorted(list_of_numbers, key=digits_sum)