from typing import Callable

def fib(mint_num: int) -> int:
    def loop_calc(x_val: int, y_val: int, count_val: int) -> int:
        if count_val > 0:
            return loop_calc(y_val, x_val + y_val, count_val - 1)
        else:
            return x_val
    return loop_calc(0, 1, mint_num)