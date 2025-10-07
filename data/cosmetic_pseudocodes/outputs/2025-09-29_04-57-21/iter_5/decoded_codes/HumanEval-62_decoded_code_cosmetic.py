from typing import List

def derivative(list_of_coefficients: List[int]) -> List[int]:
    def inner(index: int, values: List[int], result: List[int]) -> List[int]:
        if index >= len(values):
            return result
        result.append(values[index] * index)
        return inner(index + 1, values, result)
    return inner(1, list_of_coefficients, [])