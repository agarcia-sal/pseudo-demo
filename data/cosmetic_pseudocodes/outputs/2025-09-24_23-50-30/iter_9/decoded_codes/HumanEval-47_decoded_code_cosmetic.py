from typing import Iterable, Union, List

def median(elements: Iterable[Union[int, float]]) -> float:
    sorted_elements: List[Union[int, float]] = list(elements)
    sorted_elements.sort()

    count: int = len(sorted_elements)
    if (count - 1) % 2 != 0:
        middle_index: int = (count - 1) // 2
        return float(sorted_elements[middle_index])
    else:
        upper_index: int = count // 2
        lower_index: int = upper_index - 1
        sum_value: float = sorted_elements[lower_index] + sorted_elements[upper_index]
        return sum_value / 2.0