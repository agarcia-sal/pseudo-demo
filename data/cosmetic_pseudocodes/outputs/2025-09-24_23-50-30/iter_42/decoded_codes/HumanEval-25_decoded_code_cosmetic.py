from math import sqrt
from typing import List


def factorize(target_num: int) -> List[int]:
    def loop(divider: int, current_num: int) -> List[int]:
        if divider > int(sqrt(current_num)) + 1:
            return [current_num] if current_num > 1 else []
        if current_num % divider == 0:
            return [divider] + loop(divider, current_num // divider)
        return loop(divider + 1, current_num)

    factors_collection: List[int] = loop(2, target_num)
    return factors_collection