from typing import List

def derivative(array_of_terms: List[float]) -> List[float]:
    return [array_of_terms[position] * position for position in range(1, len(array_of_terms))]