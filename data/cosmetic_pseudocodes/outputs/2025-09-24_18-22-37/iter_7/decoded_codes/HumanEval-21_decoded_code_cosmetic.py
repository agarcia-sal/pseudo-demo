from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []

    smallest_value: float = list_of_numbers[0]
    index: int = 1
    while index < len(list_of_numbers):
        if list_of_numbers[index] < smallest_value:
            smallest_value = list_of_numbers[index]
        index += 1

    largest_value: float = list_of_numbers[0]
    index = 1
    while index < len(list_of_numbers):
        if largest_value < list_of_numbers[index]:
            largest_value = list_of_numbers[index]
        index += 1

    range_value: float = largest_value - smallest_value
    if range_value == 0:
        return [0.0] * len(list_of_numbers)  # All numbers equal, scale to zero

    scaled_list: List[float] = []
    counter: int = 0
    while counter < len(list_of_numbers):
        difference = list_of_numbers[counter] - smallest_value
        scaled_value = difference / range_value
        scaled_list.append(scaled_value)
        counter += 1

    return scaled_list