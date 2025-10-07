from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []
    smallest = list_of_numbers[0]
    largest = list_of_numbers[0]

    index = 1
    while index < len(list_of_numbers):
        value = list_of_numbers[index]
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
        index += 1

    range_ = largest - smallest
    normalized_values: List[float] = []
    iterator = 0
    while iterator < len(list_of_numbers):
        adjusted = list_of_numbers[iterator] - smallest
        scaled = adjusted / range_ if range_ != 0 else 0.0
        normalized_values.append(scaled)
        iterator += 1

    return normalized_values