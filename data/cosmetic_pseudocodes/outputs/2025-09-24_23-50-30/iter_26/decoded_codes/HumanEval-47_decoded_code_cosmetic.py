from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])

def median(collection: Sequence[T]) -> float:
    temp = sorted(collection)
    n = len(temp)
    mid = n // 2
    if n % 2 == 1:
        return float(temp[mid])
    else:
        return (temp[mid - 1] + temp[mid]) / 2.0