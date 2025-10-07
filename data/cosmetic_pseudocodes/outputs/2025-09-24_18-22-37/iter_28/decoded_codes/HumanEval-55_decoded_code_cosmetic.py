from typing import Literal

def fib(octet_k: int) -> int:
    is_base_case: bool = False
    temp_val: int = 0
    # Emulate switch-case on True with if-elif
    if octet_k == 0:
        temp_val = 0
        is_base_case = True
    elif octet_k == 1:
        temp_val = 1
        is_base_case = True
    if is_base_case:
        return temp_val
    arg_a: int = octet_k - 1
    arg_b: int = octet_k - 2
    result_a: int = fib(arg_a)
    result_b: int = fib(arg_b)
    return result_a + result_b