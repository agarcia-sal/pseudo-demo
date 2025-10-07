from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    result_val: int = 1

    def multiply_recursively(counter: int) -> None:
        nonlocal result_val
        if counter == integer_n:
            return
        result_val = (result_val * 2) % integer_p
        multiply_recursively(counter + 1)

    multiply_recursively(0)
    return result_val