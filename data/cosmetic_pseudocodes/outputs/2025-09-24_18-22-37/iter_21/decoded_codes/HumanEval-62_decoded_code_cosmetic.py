from typing import List

def derivative(values: List[float]) -> List[float]:
    result: List[float] = []
    position: int = 1
    while position < len(values):
        product: float = values[position] * position
        result.append(product)
        position += 1
    return result