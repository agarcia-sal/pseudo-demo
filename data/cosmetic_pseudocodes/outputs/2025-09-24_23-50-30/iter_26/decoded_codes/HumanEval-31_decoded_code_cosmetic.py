from typing import List


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    factor_set: List[int] = list(range(2, value))
    has_divisor = False
    for index in range(len(factor_set)):
        if value % factor_set[index] == 0:
            has_divisor = True
            break
    return not has_divisor