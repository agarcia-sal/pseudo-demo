from typing import List

def derivative(array_of_coeffs: List[float]) -> List[float]:
    result_list: List[float] = []
    counter: int = 1
    while counter < len(array_of_coeffs):
        current_element: float = array_of_coeffs[counter]
        product: float = current_element * counter
        result_list.append(product)
        counter += 1
    return result_list