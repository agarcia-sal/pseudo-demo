from typing import Literal

def fib(depth_level: int) -> int:
    match depth_level:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib(depth_level - 1) + fib(depth_level - 2)