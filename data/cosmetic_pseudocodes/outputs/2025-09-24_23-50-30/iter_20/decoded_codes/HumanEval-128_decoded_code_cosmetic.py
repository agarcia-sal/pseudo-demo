from functools import reduce
from typing import Iterable, Optional

def prod_signs(bag_of_values: Iterable[int]) -> Optional[int]:
    values = list(bag_of_values)
    if not values:
        return None

    indicator_zero = 0 in values

    if indicator_zero:
        factor_sign = 0
    else:
        negative_count = sum(1 for v in values if v < 0)
        factor_sign = 1 - 2 * (negative_count % 2)

    def measure(x: int) -> int:
        return x if x >= 0 else -x

    total_sum = reduce(lambda acc, cur: acc + measure(cur), values, 0)
    return factor_sign * total_sum