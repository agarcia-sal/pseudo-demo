from typing import List

def derivative(coeffs: List[float]) -> List[float]:
    def recurse(ix: int, arr: List[float], acc: List[float]) -> List[float]:
        if ix >= len(arr):
            return acc
        return recurse(ix + 1, arr, acc + [arr[ix] * ix])
    return recurse(1, coeffs, [])