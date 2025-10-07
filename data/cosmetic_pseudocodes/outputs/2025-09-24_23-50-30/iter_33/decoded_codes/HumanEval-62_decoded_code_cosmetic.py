from typing import List

def derivative(sequence_of_values: List[float]) -> List[float]:
    accumulator: List[float] = []
    for index in range(1, len(sequence_of_values)):
        multiplier = index
        value = sequence_of_values[index]
        accumulator.append(multiplier * value)
    return accumulator