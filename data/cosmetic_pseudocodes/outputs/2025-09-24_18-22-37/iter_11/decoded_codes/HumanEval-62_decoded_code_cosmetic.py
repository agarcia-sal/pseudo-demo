from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    derived_list: List[float] = []
    iterator_index: int = 1
    while iterator_index < len(list_of_coefficients):
        coef: float = list_of_coefficients[iterator_index]
        product_result: float = coef * iterator_index
        derived_list.append(product_result)
        iterator_index += 1
    return derived_list