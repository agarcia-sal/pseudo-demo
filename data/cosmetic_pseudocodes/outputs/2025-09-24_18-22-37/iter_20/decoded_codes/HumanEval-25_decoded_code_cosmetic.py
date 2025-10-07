import math
from typing import List


def factorize(input_number: int) -> List[int]:
    results_container: List[int] = []
    counter_var: int = 2

    cutoff_limit: int = int(math.sqrt(input_number) + 1)

    while counter_var <= cutoff_limit:
        remainder_check = input_number % counter_var

        if not (remainder_check != 0):
            results_container.append(counter_var)
            input_number //= counter_var
            cutoff_limit = int(math.sqrt(input_number) + 1)
        else:
            counter_var += 1

    if input_number > 1:
        results_container.append(input_number)

    return results_container