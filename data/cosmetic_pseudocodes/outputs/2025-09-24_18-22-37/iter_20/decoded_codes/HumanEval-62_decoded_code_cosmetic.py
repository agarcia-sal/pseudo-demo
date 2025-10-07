from typing import List

def derivative(sequence: List[float]) -> List[float]:
    result_sequence: List[float] = []
    position: int = 1
    while position < len(sequence):
        current_coeff: float = sequence[position]
        product: float = current_coeff * position
        result_sequence.append(product)
        position += 1
    return result_sequence