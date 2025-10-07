from typing import Iterable, List, Union


def median(input_collection: Iterable[Union[int, float]]) -> float:
    ordered_elements: List[Union[int, float]] = sorted(input_collection)
    count: int = len(ordered_elements)
    middle_index: float = count / 2

    if count % 2 != 0:
        return float(ordered_elements[int(middle_index)])
    else:
        first_middle_value: Union[int, float] = ordered_elements[int(middle_index) - 1]
        second_middle_value: Union[int, float] = ordered_elements[int(middle_index)]
        return (first_middle_value + second_middle_value) / 2.0