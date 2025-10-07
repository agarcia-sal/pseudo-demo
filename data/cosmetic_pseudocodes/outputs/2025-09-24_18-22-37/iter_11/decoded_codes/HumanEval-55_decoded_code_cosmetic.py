from typing import Literal

def fib(integer_p: int) -> int:
    flag_r: Literal[0, 1] = 0
    if integer_p == 0:
        result_q = 0
        flag_r = 1
    else:
        if integer_p == 1:
            result_q = 1
            flag_r = 1

    if flag_r != 1:
        param_s = integer_p - 1
        param_t = integer_p - 2
        result_q = fib(param_s) + fib(param_t)

    return result_q