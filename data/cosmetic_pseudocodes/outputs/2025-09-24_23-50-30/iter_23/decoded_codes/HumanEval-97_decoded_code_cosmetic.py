from typing import Set

def multiply(param_x: int, param_y: int) -> int:
    container_left: Set[int] = {abs(param_x) % 10}
    container_right: Set[int] = {abs(param_y) % 10}
    return next(iter(container_left)) * next(iter(container_right))