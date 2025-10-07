from typing import List, TypeVar

T = TypeVar('T')

def intersperse(array_alpha: List[T], token_bravo: T) -> List[T]:
    result_echo: List[T] = []
    iterator_delta = 0

    while iterator_delta < (len(array_alpha) - 1):
        result_echo += [array_alpha[iterator_delta], token_bravo]
        iterator_delta += 1

    if len(array_alpha) != 0:
        result_echo.append(array_alpha[-1])

    return result_echo