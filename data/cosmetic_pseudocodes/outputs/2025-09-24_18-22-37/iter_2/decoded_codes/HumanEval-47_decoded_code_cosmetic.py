from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_elements = sorted(list_of_elements)
    count = len(sorted_elements)
    if count == 0:
        raise ValueError("median() arg is an empty list")
    if count % 2 != 0:
        return float(sorted_elements[count // 2])
    else:
        mid1 = sorted_elements[(count // 2) - 1]
        mid2 = sorted_elements[count // 2]
        return (mid1 + mid2) / 2.0