from typing import List

def derivative(a: List[float]) -> List[float]:
    return [a[b] * b for b in range(1, len(a))]