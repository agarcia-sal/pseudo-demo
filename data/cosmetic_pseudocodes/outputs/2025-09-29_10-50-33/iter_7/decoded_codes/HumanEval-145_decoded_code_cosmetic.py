from functools import reduce
from typing import Iterable, List

def order_by_points(series_of_values: Iterable[int]) -> List[int]:
    def total_digits(value: int) -> int:
        polarity = 1
        if value < 0:
            value = -value
            polarity = -1
        numeral_components = [int(d) for d in str(value)]
        numeral_components[0] *= polarity
        return reduce(lambda acc, el: acc + el, numeral_components, 0)
    return sorted(series_of_values, key=total_digits)