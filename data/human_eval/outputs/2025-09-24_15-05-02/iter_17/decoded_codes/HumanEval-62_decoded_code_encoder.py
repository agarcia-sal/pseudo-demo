from typing import List

def derivative(xs: List[float]) -> List[float]:
    return [index * value for index, value in enumerate(xs, start=1)]