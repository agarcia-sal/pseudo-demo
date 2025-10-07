from typing import List

def derivative(xs: List[float]) -> List[float]:
    result = []
    for i, x in enumerate(xs):
        result.append(i * x)
    return result[1:]