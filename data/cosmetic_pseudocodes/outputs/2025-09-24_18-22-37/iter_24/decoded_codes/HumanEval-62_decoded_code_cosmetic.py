from typing import List


def derivative(list_of_coefficients: List[float]) -> List[float]:
    result_list: List[float] = []
    position_counter: int = 0

    while position_counter < len(list_of_coefficients):
        if position_counter != 0:
            intermediate_value = list_of_coefficients[position_counter]
            multiplied_value = intermediate_value * position_counter
            result_list.append(multiplied_value)
        position_counter += 1

    return result_list