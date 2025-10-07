from functools import reduce
from typing import List

def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor_list: List[int] = [i for i in range(2, value)]
    def reduction_function(accumulator: bool, current: int) -> bool:
        return accumulator and (value % current != 0)
    return reduce(reduction_function, divisor_list, True)