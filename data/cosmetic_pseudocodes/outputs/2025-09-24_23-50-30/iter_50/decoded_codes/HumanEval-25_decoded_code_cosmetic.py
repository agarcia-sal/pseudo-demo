import math
from typing import List


def factorize(integer_n: int) -> List[int]:
    result_list: List[int] = []
    current_candidate: int = 2
    limit_value: int = int(math.isqrt(integer_n)) + 1
    while current_candidate <= limit_value and integer_n > 1:
        if integer_n % current_candidate == 0:
            result_list.append(current_candidate)
            integer_n //= current_candidate
            limit_value = int(math.isqrt(integer_n)) + 1
        else:
            current_candidate += 1
    if integer_n > 1:
        result_list.append(integer_n)
    return result_list