from typing import List

def derivative(xs: List[float]) -> List[float]:
    return [i * x for i, x in enumerate(xs)][1:]