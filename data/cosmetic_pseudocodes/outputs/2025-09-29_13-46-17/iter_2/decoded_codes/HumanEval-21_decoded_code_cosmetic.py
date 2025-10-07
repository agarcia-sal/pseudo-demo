from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []

    min_val: float = list_of_numbers[0]
    max_val: float = list_of_numbers[0]

    def find_min_max(index: int) -> None:
        nonlocal min_val, max_val
        if index == len(list_of_numbers):
            return
        if list_of_numbers[index] < min_val:
            min_val = list_of_numbers[index]
        if list_of_numbers[index] > max_val:
            max_val = list_of_numbers[index]
        find_min_max(index + 1)

    find_min_max(1)

    def transform_to_unit(idx: int) -> List[float]:
        if idx == len(list_of_numbers):
            return []
        element = list_of_numbers[idx]
        # Avoid division by zero when all elements are equal
        if max_val == min_val:
            scaled = 0.0
        else:
            scaled = (element - min_val) / (max_val - min_val)
        return [scaled] + transform_to_unit(idx + 1)

    return transform_to_unit(0)