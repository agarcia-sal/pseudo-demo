from typing import List

def derivative(alpha: List[float]) -> List[float]:
    return [alpha[index] * index for index in range(1, len(alpha))]