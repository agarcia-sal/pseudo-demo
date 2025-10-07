from typing import List

def derivative(array_of_terms: List[int]) -> List[int]:
    result_list: List[int] = []
    pos_counter: int = 1
    while pos_counter < len(array_of_terms):
        current_value: int = array_of_terms[pos_counter]
        multiplied_value: int = current_value * pos_counter
        result_list.append(multiplied_value)
        pos_counter += 1
    return result_list