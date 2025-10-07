from typing import Iterable, List, Union


def custom_sort_method(collection: List[Union[int, float]]) -> List[Union[int, float]]:
    # Basic implementation of a sorting algorithm (e.g., Timsort via built-in sorted)
    # Presuming 'custom_sort_method' abstracts the sorting logic
    return sorted(collection)


def median(original_collection: Iterable[Union[int, float]]) -> float:
    sorted_collection: List[Union[int, float]] = []
    for element in original_collection:
        sorted_collection.append(element)

    sorted_collection = custom_sort_method(sorted_collection)

    size_value: int = len(sorted_collection)
    midpoint: int = size_value // 2

    if size_value % 2 != 0:
        median_value: float = float(sorted_collection[midpoint])
        return median_value
    else:
        first_middle_element: Union[int, float] = sorted_collection[midpoint - 1]
        second_middle_element: Union[int, float] = sorted_collection[midpoint]
        median_value: float = (first_middle_element + second_middle_element) / 2.0
        return median_value