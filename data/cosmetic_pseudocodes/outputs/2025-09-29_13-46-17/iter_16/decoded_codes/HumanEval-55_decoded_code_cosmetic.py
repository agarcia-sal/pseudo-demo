from typing import Callable

def fib(integer_n: int) -> int:
    def ψₓ₈(a_β: int) -> int:
        if not (a_β > 1):
            if a_β < 1:
                return 0
            else:
                return 1
        else:
            return ψₓ₈(a_β - 1) + ψₓ₈(a_β - 2)
    return ψₓ₈(integer_n)