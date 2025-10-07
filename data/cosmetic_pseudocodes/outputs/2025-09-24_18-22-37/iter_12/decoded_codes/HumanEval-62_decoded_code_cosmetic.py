from typing import List

def derivative(array_of_elements: List[float]) -> List[float]:
    result: List[float] = []
    position: int = 1
    while position < len(array_of_elements):
        multiplier: int = position
        current_value: float = array_of_elements[position]
        product: float = multiplier * current_value
        result.append(product)
        position += 1
    return result