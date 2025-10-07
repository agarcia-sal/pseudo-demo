from typing import Sequence, TypeVar

T = TypeVar('T')

def strlen(input_variable: Sequence[T]) -> int:
    index_counter = 0
    while True:
        try:
            _ = input_variable[index_counter]
        except IndexError:
            break
        index_counter += 1
    return index_counter