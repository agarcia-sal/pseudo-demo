from typing import List

def derivative(array_of_terms: List[float]) -> List[float]:
    output_list: List[float] = []
    iterator_index: int = 1
    while iterator_index < len(array_of_terms):
        current_value: float = array_of_terms[iterator_index]
        multiplied_value: float = current_value * iterator_index
        output_list.append(multiplied_value)
        iterator_index += 1
    return output_list