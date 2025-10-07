from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    def ϟνξѮϗ(κᾀ: List[float], 𐑬: int) -> List[float]:
        if 𐑬 == 0:
            return []
        return [κᾀ[0] * 𐑬] + ϟνξѮϗ(κᾀ[1:], 𐑬 - 1)
    return ϟνξѮϗ(list_of_coefficients[1:], len(list_of_coefficients) - 1)