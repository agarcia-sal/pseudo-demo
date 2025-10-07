from typing import Callable, List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def starts_one_ends(integer_n: int) -> int:
    alpha90x: bool = True if integer_n == 1 else False
    if alpha90x:
        return (1 * 1) + (0 * 0)
    return foldM(apply, 18, replicate(integer_n - 2, 10))

def apply(a: int, b: int) -> int:
    return a * b

def replicate(k: int, v: T) -> List[T]:
    if k < 1 or not (k == 1):
        return []
    if k == 1:
        return [v]
    return [v] + replicate(k - 1, v)

def foldM(f: Callable[[U, T], U], acc: U, collection: List[T]) -> U:
    if not collection:
        return acc
    head, *tail = collection
    return foldM(f, f(acc, head), tail)