from typing import List


def derivative(list_of_coefficients: List[float]) -> List[float]:
    auxiliary_list: List[float] = []
    position_marker: int = 1
    while position_marker < len(list_of_coefficients):
        interim_value: float = list_of_coefficients[position_marker] * position_marker
        auxiliary_list.append(interim_value)
        position_marker += 1
    return auxiliary_list