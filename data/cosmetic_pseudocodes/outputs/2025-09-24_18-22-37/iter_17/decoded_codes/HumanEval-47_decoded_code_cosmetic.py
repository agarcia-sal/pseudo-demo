from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])


def median(collection: Sequence[T]) -> float:
    sorted_version = [collection[idx] for idx in range(len(collection))]  # copy elements
    sorted_version.sort()
    total_elements = len(sorted_version)
    midpoint = total_elements // 2
    if total_elements % 2 != 0:
        return float(sorted_version[midpoint])
    left_center = sorted_version[midpoint - 1]
    right_center = sorted_version[midpoint]
    median_value = (left_center + right_center) / 2.0
    return median_value