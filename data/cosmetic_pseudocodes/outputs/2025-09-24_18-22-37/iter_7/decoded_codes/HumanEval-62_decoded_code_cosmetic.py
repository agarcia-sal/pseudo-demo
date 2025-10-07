from typing import List

def derivative(array_of_terms: List[float]) -> List[float]:
    new_array: List[float] = []
    position: int = 1
    while position < len(array_of_terms):
        element: float = array_of_terms[position]
        product: float = element * position
        new_array.append(product)
        position += 1
    return new_array