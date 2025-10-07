from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_elements = sorted(list_of_elements)
    count = len(sorted_elements)
    middle_position = count // 2

    if count % 2 != 0:
        return float(sorted_elements[middle_position])

    first_mid_val = sorted_elements[middle_position - 1]
    second_mid_val = sorted_elements[middle_position]

    return (first_mid_val + second_mid_val) * 0.5