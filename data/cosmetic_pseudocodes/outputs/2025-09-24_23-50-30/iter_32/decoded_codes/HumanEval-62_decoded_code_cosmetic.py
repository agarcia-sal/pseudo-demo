from typing import List

def derivative(array_of_numbers: List[float]) -> List[float]:
    index_counter: int = 1
    new_sequence: List[float] = []
    while index_counter < len(array_of_numbers):
        new_sequence.append(array_of_numbers[index_counter] * index_counter)
        index_counter += 1
    return new_sequence