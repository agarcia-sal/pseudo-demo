from typing import List

def derivative(inputs: List[float]) -> List[float]:
    result: List[float] = []
    position: int = 1
    while position < len(inputs):
        result.append(inputs[position] * position)
        position += 1
    return result