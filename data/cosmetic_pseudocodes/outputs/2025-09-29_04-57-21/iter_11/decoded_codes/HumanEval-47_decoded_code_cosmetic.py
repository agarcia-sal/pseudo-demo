from typing import Iterable, TypeVar, Union, List

T = TypeVar("T", bound=Union[int, float])

def median(collection: Iterable[T]) -> float:
    ordered_collection: List[T] = sorted(collection)
    count: int = len(ordered_collection)
    if count % 2 != 0:
        center: int = count // 2
        return float(ordered_collection[center])
    mid_point: int = count // 2
    return (ordered_collection[mid_point - 1] + ordered_collection[mid_point]) * 0.5