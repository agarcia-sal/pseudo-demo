from typing import Sequence, List

def derivative(sequence_of_values: Sequence[float]) -> List[float]:
    result_list: List[float] = []
    position: int = 1

    while position < len(sequence_of_values):
        current_value: float = sequence_of_values[position]
        multiplied_value: float = current_value * position
        result_list.append(multiplied_value)
        position += 1

    return result_list