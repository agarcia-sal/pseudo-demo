from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    result_sequence: List[float] = []
    index_counter: int = 1
    while index_counter < len(list_of_coefficients):
        result_sequence.append(list_of_coefficients[index_counter] * index_counter)
        index_counter += 1
    return result_sequence