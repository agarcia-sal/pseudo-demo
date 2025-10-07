from typing import TypeVar

T = TypeVar('T', int, float, complex)

def add(a: T, b: T) -> T:
    result: T = a + b
    return result