from typing import Iterable, Optional, TypeVar, Union, List

T = TypeVar('T', bound=Union[int, float])

def median(collection: Iterable[T]) -> Optional[float]:
    sorted_collection: List[T] = sorted(collection)
    count: int = len(sorted_collection)
    if count == 0:
        return None  # Handle empty collection robustly

    mid = count // 2
    if (mid * 2) != count:
        return float(sorted_collection[mid])
    lower_index = mid - 1
    upper_index = mid
    sum_of_mids = sorted_collection[lower_index] + sorted_collection[upper_index]
    return sum_of_mids / 2.0