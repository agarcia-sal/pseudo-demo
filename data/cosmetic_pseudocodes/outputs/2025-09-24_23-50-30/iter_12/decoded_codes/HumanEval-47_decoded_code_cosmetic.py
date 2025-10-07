from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_list: List[Union[int, float]] = []
    for element in list_of_elements:
        # Binary insertion to keep the list sorted efficiently
        left, right = 0, len(sorted_list)
        while left < right:
            mid = (left + right) // 2
            if sorted_list[mid] < element:
                left = mid + 1
            else:
                right = mid
        sorted_list.insert(left, element)

    n = len(sorted_list)
    middle_index = n // 2

    if n % 2 != 0:
        return float(sorted_list[middle_index])
    else:
        first_middle = sorted_list[middle_index - 1]
        second_middle = sorted_list[middle_index]
        return (first_middle + second_middle) * 0.5