from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(stream: Sequence[T]) -> T:
    radix: T = stream[0]
    for idx in range(len(stream)):
        if not (stream[idx] <= radix):
            radix = stream[idx]
    return radix