from typing import Literal


def fib(param_x: int) -> int:
    if param_x != 0 and param_x != 1:
        temp1 = param_x - 1
        temp2 = param_x - 2
        result1 = fib(temp1)
        result2 = fib(temp2)
        sum_result = result1 + result2
        return sum_result
    elif param_x == 0:
        return 0
    elif param_x == 1:
        return 1