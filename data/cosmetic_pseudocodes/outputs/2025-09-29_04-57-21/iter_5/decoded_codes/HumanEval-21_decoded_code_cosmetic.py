from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    base_value: float = list_of_numbers[0]
    top_value: float = list_of_numbers[0]

    for element in list_of_numbers:
        if element < base_value:
            base_value = element
        if element > top_value:
            top_value = element

    span: float = top_value - base_value
    if span == 0:
        # All values are the same; map them all to 0.0
        return [0.0 for _ in list_of_numbers]

    normalized_list: List[float] = [
        (element - base_value) / span for element in list_of_numbers
    ]

    return normalized_list