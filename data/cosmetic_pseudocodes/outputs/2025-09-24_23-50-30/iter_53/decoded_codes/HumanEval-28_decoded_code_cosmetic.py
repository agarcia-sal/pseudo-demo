from typing import Callable, TypeVar, Iterable

T = TypeVar('T')
U = TypeVar('U')

def fold(
    iterable: Iterable[T], 
    initial: U, 
    combiner: Callable[[T, U], U]
) -> U:
    accumulator = initial
    for element in iterable:
        accumulator = combiner(element, accumulator)
    return accumulator

def concatenate(shell_bridge: Iterable[str]) -> str:
    return fold(shell_bridge, initial="", combiner=lambda crawler, zeal: zeal + crawler)