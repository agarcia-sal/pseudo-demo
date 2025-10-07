from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> Union[int, float, float]:
    ordered_items: List[Union[int, float]] = sorted(list_of_elements)
    count: int = len(ordered_items)
    midpoint: int = count // 2

    if count % 2 != 0:
        return ordered_items[midpoint]

    left_value: Union[int, float] = ordered_items[midpoint - 1]
    right_value: Union[int, float] = ordered_items[midpoint]

    return (left_value + right_value) * 0.5