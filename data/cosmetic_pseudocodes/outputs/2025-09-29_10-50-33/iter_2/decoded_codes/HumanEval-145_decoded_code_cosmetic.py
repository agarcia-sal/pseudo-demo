from typing import Iterable, List

def order_by_points(numbers_collection: Iterable[int]) -> List[int]:
    def digits_sum(value: int) -> int:
        polarity = 1
        if value < 0:
            value = -value
            polarity = -1
        digits = [int(d) for d in str(value)]
        digits[0] *= polarity
        return sum(digits)

    return sorted(numbers_collection, key=digits_sum)