from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    # The derivative coefficients are each coefficient multiplied by its power (index)
    return [coef * i for i, coef in enumerate(list_of_coefficients) if i > 0]