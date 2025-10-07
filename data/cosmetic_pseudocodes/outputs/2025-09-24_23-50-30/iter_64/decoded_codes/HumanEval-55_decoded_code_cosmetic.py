from typing import Literal


def fib(step: int) -> int:
    match step:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            alpha: int = step - 1
            beta: int = step - 2
            delta: int = fib(alpha)
            gamma: int = fib(beta)
            return delta + gamma