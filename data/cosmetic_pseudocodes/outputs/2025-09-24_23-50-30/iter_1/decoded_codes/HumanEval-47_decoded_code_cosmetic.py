from typing import List, Union, Sequence

def median(list_of_elements: Sequence[Union[int, float]]) -> float:
    sorted_list = list(list_of_elements)
    sorted_list.sort()
    n = len(sorted_list)
    if n == 0:
        raise ValueError("median() arg is an empty sequence")
    if n % 2 != 0:
        middle = (n - 1) // 2
        return float(sorted_list[middle])
    else:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return (sorted_list[mid1] + sorted_list[mid2]) / 2.0