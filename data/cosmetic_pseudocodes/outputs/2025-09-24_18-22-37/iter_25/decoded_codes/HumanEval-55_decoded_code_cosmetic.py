from typing import SupportsIndex

def fib(param_z: SupportsIndex) -> int:
    n = int(param_z)  # Ensure integer input
    if n == 0:
        return 0
    if n == 1:
        return 1
    temp_a = n - 1
    result_1 = fib(temp_a)
    temp_b = n - 2
    result_2 = fib(temp_b)
    final_sum = result_1 + result_2
    return final_sum