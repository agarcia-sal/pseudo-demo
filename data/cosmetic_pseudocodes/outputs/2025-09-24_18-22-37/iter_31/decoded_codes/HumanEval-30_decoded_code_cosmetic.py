from typing import List

def get_positive(array_of_values: List[float]) -> List[float]:
    positive_container: List[float] = []
    for single_value in array_of_values:
        if single_value > 0:
            positive_container.append(single_value)
    return positive_container