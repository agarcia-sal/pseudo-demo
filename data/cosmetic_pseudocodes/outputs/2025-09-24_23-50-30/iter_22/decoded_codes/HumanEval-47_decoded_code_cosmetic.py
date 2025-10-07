from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    delta: int = len(list_of_elements)
    epsilon: List[Union[int, float]] = sorted(list_of_elements)
    if delta % 2 == 1:
        omega: int = delta // 2
        return float(epsilon[omega])
    else:
        alpha: int = delta // 2
        beta: int = alpha - 1
        return (epsilon[beta] + epsilon[alpha]) / 2.0