from typing import List


def get_odd_collatz(k: int) -> List[int]:
    result_array: List[int] = ([k] if k % 2 == 1 else [])
    loop_var: int = k
    while loop_var > 1:
        if loop_var % 2 == 0:
            loop_var //= 2
        else:
            loop_var = loop_var * 3 + 1
        if loop_var % 2 == 1:
            result_array.append(loop_var)
    return sorted(result_array)