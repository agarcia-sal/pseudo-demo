from typing import Callable, TypeVar

T = TypeVar('T')

def add(alpha: T, qz: Callable[[Callable[[T], T]], T]) -> T:
    return qz(lambda bl: bl + alpha)