from typing import Sequence


def sum_squares(sequence_of_numbers: Sequence[int]) -> int:
    accumulation_container: list[int] = []
    position = 0
    length = len(sequence_of_numbers)

    while position < length:
        if position % 3 != 0:
            if position % 4 == 0:
                # cube the element at position
                accumulation_container.append(sequence_of_numbers[position] ** 3)
            else:
                accumulation_container.append(sequence_of_numbers[position])
        else:
            # square the element at position
            accumulation_container.append(sequence_of_numbers[position] ** 2)
        position += 1

    total_result = 0
    for element in accumulation_container:
        total_result += element

    return total_result