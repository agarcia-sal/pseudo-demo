from typing import Any

def fib(param_x: int) -> int:
    if param_x == 0:
        label_result: int = 0
    elif param_x == 1:
        label_result = 1
    else:
        label_temp1: int = fib(param_x - 1)
        label_temp2: int = fib(param_x - 2)
        label_result = label_temp1 + label_temp2
    return label_result