from typing import List

def derivative(list_of_coefficients: List[int]) -> List[int]:
    def compute_derivative_term(collection: List[int], position: int, accumulator: List[int]) -> List[int]:
        if position == len(collection):
            return accumulator
        updated_accumulator = accumulator + [collection[position] * position]
        return compute_derivative_term(collection, position + 1, updated_accumulator)
    return compute_derivative_term(list_of_coefficients, 1, [])