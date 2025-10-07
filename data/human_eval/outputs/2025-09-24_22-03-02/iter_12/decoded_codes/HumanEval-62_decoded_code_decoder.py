from typing import List

def derivative(xs: List[float]) -> List[float]:
    result: List[float] = []
    for i in range(len(xs) - 1):
        if i > 0:
            result.append(i * xs[i])
    return result