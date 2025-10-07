from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1

    def iterate(index: int) -> int:
        nonlocal accumulator
        if not (index < integer_n):
            return accumulator
        accumulator = ((accumulator << 1) - ((accumulator << 1) // integer_p) * integer_p)
        return iterate(index + 1)

    return iterate(0)