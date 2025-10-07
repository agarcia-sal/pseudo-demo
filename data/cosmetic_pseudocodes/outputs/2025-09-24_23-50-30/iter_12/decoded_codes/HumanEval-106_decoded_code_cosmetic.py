from functools import reduce
from typing import List

def f(number_end: int) -> List[int]:

    def compute_factorial(current_num: int) -> int:
        if current_num < 2:
            return 1
        else:
            return current_num * compute_factorial(current_num - 1)

    def compute_sum(limit_num: int) -> int:
        seq = [x for x in range(1, limit_num + 1)]
        return reduce(lambda acc, val: acc + val, seq, 0)

    output_array: List[int] = []
    counter: int = 1

    while counter <= number_end:
        is_even_flag = not (counter % 2 == 1)
        value_result = compute_factorial(counter) if is_even_flag else compute_sum(counter)
        output_array.append(value_result)
        counter += 1

    return output_array