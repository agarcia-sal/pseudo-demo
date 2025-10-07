from typing import List

def derivative(array_of_numbers: List[float]) -> List[float]:
    result_array: List[float] = []
    index_counter: int = 1
    while index_counter < len(array_of_numbers):
        temp_product: float = array_of_numbers[index_counter] * index_counter
        result_array.append(temp_product)
        index_counter += 1
    return result_array