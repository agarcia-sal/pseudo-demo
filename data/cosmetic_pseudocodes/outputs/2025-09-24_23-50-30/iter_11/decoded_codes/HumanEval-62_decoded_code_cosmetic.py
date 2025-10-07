from collections import deque
from typing import List


def derivative(array_of_values: List[float]) -> List[float]:
    result_structure: deque[float] = deque()
    position: int = 1
    while position < len(array_of_values):
        result_structure.append(array_of_values[position] * position)
        position += 1
    return list(result_structure)