from typing import List

def derivative(coef_list: List[float]) -> List[float]:
    result_list: List[float] = []
    position: int = 0
    while position < len(coef_list) - 1:
        position += 1
        result_list.append(position * coef_list[position])
    return result_list