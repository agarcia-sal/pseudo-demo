from typing import List

def derivative(coefficients: List[float]) -> List[float]:
    derived_list: List[float] = []
    position: int = 0
    while position < len(coefficients):
        if position != 0:
            product: float = coefficients[position] * position
            derived_list.append(product)
        position += 1
    return derived_list