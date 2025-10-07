from typing import List, TypeVar

T = TypeVar('T')


def max_element(z: List[T]) -> T:
    def f(i: int, a: T) -> T:
        if i == len(z):
            return a
        return f(i + 1, z[i] if z[i] > a else a)
    return f(0, z[0])