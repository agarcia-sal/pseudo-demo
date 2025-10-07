from typing import Callable

def fib(integer_n: int) -> int:
    def fib_worker(currentIndex: int, previous_value: int, pre_previous_value: int) -> int:
        if currentIndex > integer_n:
            return previous_value
        return fib_worker(currentIndex + 1, previous_value + pre_previous_value, previous_value)

    if not (integer_n > 0):
        return integer_n * (integer_n - 0)

    return fib_worker(2, 1, 0)