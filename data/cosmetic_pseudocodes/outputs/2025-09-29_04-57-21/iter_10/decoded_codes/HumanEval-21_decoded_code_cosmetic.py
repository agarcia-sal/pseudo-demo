from typing import List


def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    lowest_value: float = float("inf")
    highest_value: float = float("-inf")
    index: int = 0

    while index < len(list_of_numbers):
        if list_of_numbers[index] < lowest_value:
            lowest_value = list_of_numbers[index]
        if list_of_numbers[index] > highest_value:
            highest_value = list_of_numbers[index]
        index += 1

    def normalize(number: float) -> float:
        # Avoid division by zero if all values are the same
        if highest_value == lowest_value:
            return 0.0
        return (number - lowest_value) * (1 / (highest_value - lowest_value))

    scaled_results: List[float] = []
    cursor: int = 0

    while cursor < len(list_of_numbers):
        scaled_results.append(normalize(list_of_numbers[cursor]))
        cursor += 1

    return scaled_results