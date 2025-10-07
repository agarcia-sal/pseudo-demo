from typing import Sequence


def sum_squares(array_of_numbers: Sequence[float]) -> float:
    accumulated_values: list[float] = []
    position: int = 0
    while position < len(array_of_numbers):
        divisible_by_three = (position % 3 == 0)
        divisible_by_four = (position % 4 == 0)
        if divisible_by_three:
            accumulated_values.append(array_of_numbers[position] ** 2)
        elif divisible_by_four and not divisible_by_three:
            accumulated_values.append(array_of_numbers[position] ** 3)
        else:
            accumulated_values.append(array_of_numbers[position])
        position += 1
    total_sum: float = 0.0
    for element in accumulated_values:
        total_sum += element
    return total_sum