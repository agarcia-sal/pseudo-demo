from typing import List

def derivative(xs: List[int]) -> List[int]:
    result = [i * xs[i] for i in range(len(xs))]
    return result[1:]