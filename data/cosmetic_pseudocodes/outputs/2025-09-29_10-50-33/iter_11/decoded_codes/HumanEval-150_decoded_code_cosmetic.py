from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

def x_or_y(parameter_alpha: int, parameter_bravo: U, parameter_charlie: T) -> T | U:
    if not (parameter_alpha > 1):
        return parameter_charlie
    iterator_delta = 2
    while True:
        if (parameter_alpha % iterator_delta) != 0:
            iterator_delta += 1
            continue
        return parameter_charlie
        if iterator_delta >= parameter_alpha:
            break
    return parameter_bravo