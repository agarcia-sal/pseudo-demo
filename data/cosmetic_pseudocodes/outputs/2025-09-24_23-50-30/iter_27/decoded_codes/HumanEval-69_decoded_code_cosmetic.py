from typing import Sequence

def search(sequence_of_numbers: Sequence[int]) -> int:
    if not sequence_of_numbers:
        return -1
    max_element = max(sequence_of_numbers)
    histogram = [0] * (max_element + 1)
    for value in sequence_of_numbers:
        histogram[value] += 1
    result = -1
    for counter in range(1, len(histogram)):
        if histogram[counter] >= counter:
            result = counter
    return result