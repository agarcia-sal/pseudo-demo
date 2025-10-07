from math import floor, sqrt
from typing import List


def factorize(integer_z: int) -> List[int]:
    result_set: List[int] = []

    def factor_recur(counter_a: int, value_b: int) -> None:
        if counter_a <= floor(sqrt(value_b)) + 1:
            if value_b % counter_a == 0:
                factor_recur(counter_a, value_b // counter_a)
                result_set.append(counter_a)
            else:
                factor_recur(counter_a + 1, value_b)
        else:
            if value_b > 1:
                result_set.append(value_b)

    factor_recur(2, integer_z)
    return result_set