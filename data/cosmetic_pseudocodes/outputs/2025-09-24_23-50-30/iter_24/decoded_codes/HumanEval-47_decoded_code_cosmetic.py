from typing import Sequence, Union

def median(array_of_items: Sequence[Union[int, float]]) -> float:
    sorted_items = sorted(array_of_items)
    count = len(sorted_items)
    if count == 0:
        raise ValueError("median() arg is an empty sequence")
    if count % 2 != 0:
        # Odd length: return middle element
        middle_index = (count - (count // 2) * 2) + (count // 2) - 1
        return float(sorted_items[middle_index])
    else:
        # Even length: return average of two middle elements
        first_index = (count // 2) - 1
        second_index = first_index + 1
        return (sorted_items[first_index] + sorted_items[second_index]) / 2.0