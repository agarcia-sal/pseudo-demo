from typing import List

def derivative(array_of_values: List[float]) -> List[float]:
    def helper(index_var: int, accumulator_var: List[float]) -> List[float]:
        if index_var >= len(array_of_values):
            return accumulator_var
        else:
            return helper(index_var + 1, accumulator_var + [array_of_values[index_var] * index_var])
    return helper(1, [])