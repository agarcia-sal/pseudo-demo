from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    list_of_products: List[float] = []
    position: int = 1
    while position < len(list_of_coefficients):
        list_of_products.append(list_of_coefficients[position] * position)
        position += 1
    return list_of_products