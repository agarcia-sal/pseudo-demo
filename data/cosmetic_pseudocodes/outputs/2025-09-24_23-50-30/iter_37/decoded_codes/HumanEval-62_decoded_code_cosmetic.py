from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    def recurse(index: int, lst: List[float], acc: List[float]) -> List[float]:
        if index >= len(lst):
            return acc
        else:
            return recurse(index + 1, lst, acc + [lst[index] * index])
    return recurse(1, list_of_coefficients, [])