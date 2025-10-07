from typing import List

def rescale_to_unit(array_of_values: List[float]) -> List[float]:
    alpha: float = array_of_values[0]
    beta: float = array_of_values[0]
    for index in range(1, len(array_of_values)):
        if array_of_values[index] < alpha:
            alpha = array_of_values[index]
        elif array_of_values[index] > beta:
            beta = array_of_values[index]
    divisor: float = beta - alpha
    scaled_list: List[float] = []
    pointer: int = 0
    while pointer < len(array_of_values):
        scaled_list.append((array_of_values[pointer] - alpha) / divisor)
        pointer += 1
    return scaled_list