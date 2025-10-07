from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    output_sequence: List[float] = []
    iterator_index: int = 1
    while iterator_index < len(list_of_coefficients):
        output_sequence.append(iterator_index * list_of_coefficients[iterator_index])
        iterator_index += 1
    return output_sequence