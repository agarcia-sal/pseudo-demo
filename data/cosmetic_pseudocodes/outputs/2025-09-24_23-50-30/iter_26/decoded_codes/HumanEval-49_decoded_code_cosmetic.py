from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    def recur_func(counter: int, acc: int) -> int:
        if counter == integer_n:
            return acc
        else:
            return recur_func(counter + 1, (acc * 2) % integer_p)
    return recur_func(0, 1)