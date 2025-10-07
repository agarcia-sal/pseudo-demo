from typing import List

def derivative(array_of_terms: List[int]) -> List[int]:
    transformed_list: List[int] = []
    idx: int = 1
    while idx < len(array_of_terms):
        product: int = array_of_terms[idx] * idx
        transformed_list.append(product)
        idx += 1
    return transformed_list