from typing import List


def derivative(list_of_coefficients: List[int]) -> List[int]:
    def recur_derivative(index: int, coefficients: List[int], accumulator: List[int]) -> List[int]:
        if index == len(coefficients):
            return accumulator
        updated_accumulator = accumulator + [coefficients[index] * index]
        return recur_derivative(index + 1, coefficients, updated_accumulator)

    return recur_derivative(1, list_of_coefficients, [])