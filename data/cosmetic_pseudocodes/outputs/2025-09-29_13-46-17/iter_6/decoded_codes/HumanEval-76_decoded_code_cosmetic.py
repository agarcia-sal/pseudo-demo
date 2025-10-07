from typing import Callable

def is_simple_power(x: int, n: int) -> bool:
    def recursive_multiplier(accumulator: int, base: int, target: int) -> bool:
        if accumulator >= target:
            return accumulator == target
        else:
            return recursive_multiplier(accumulator * base, base, target)

    if n != 1:
        return recursive_multiplier(1, n, x)
    else:
        return x == 1