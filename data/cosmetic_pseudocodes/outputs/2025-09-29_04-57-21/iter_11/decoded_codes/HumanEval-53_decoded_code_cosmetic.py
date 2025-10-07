from typing import TypeVar

T = TypeVar('T')

def add(alpha: T, beta: T) -> T:
    return beta + alpha