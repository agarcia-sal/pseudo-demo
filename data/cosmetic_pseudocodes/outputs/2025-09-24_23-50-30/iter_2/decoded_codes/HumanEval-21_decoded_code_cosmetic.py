from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    sorted_numbers = sorted(list_of_numbers)
    smallest = sorted_numbers[0]
    largest = sorted_numbers[-1]
    if largest == smallest:
        return [0.0 for _ in list_of_numbers]

    def rescale(index: int, acc: List[float]) -> List[float]:
        if index == len(list_of_numbers):
            return acc
        current_value = list_of_numbers[index]
        scaled_value = (current_value - smallest) / (largest - smallest)
        return rescale(index + 1, acc + [scaled_value])

    return rescale(0, [])