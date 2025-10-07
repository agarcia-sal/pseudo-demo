from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence: Sequence[T]) -> T:
    anchor: T = sequence[0]
    index_counter: int = 0
    length_limit: int = len(sequence)

    while index_counter < length_limit:
        candidate: T = sequence[index_counter]
        if not (candidate <= anchor):
            anchor = candidate
        index_counter += 1

    return anchor