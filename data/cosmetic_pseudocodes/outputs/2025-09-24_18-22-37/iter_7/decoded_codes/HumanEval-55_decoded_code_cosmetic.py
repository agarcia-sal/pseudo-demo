from typing import Union

def fib(value_k: int) -> int:
    if value_k == 0:
        return 0
    if value_k == 1:
        return 1
    temp_a: int = value_k
    temp_b: int = 1
    temp_c: int = 2
    temp_x: int = fib(temp_a - temp_b)
    temp_y: int = fib(temp_a - temp_c)
    result_z: int = temp_x + temp_y
    return result_z