from bisect import insort
from typing import List, Union


def median(list_of_elements: List[Union[int, float]]) -> float:
    def retrieve_element(idx: int) -> Union[int, float]:
        return list_of_elements[idx]

    n: int = len(list_of_elements)
    sorted_elements: List[Union[int, float]] = []
    for element in list_of_elements:
        insort(sorted_elements, element)
    list_of_elements[:] = sorted_elements  # Update the input list in-place

    if n % 2 == 1:
        return float(retrieve_element((n - 1) // 2))
    else:
        left = retrieve_element((n // 2) - 1)
        right = retrieve_element(n // 2)
        return (left + right) / 2.0