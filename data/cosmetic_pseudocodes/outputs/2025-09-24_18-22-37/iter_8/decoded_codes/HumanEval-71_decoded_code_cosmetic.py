from math import sqrt
from typing import Union

def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    epsilon: int = 2
    half_perimeter: float = (alpha + beta + gamma) / 2
    if (alpha + beta) > gamma:
        if (beta + gamma) > alpha:
            if (gamma + alpha) > beta:
                p_minus_alpha: float = half_perimeter - alpha
                p_minus_beta: float = half_perimeter - beta
                p_minus_gamma: float = half_perimeter - gamma
                multiplied_terms: float = half_perimeter * p_minus_alpha * p_minus_beta * p_minus_gamma
                root_of_multiplied: float = sqrt(multiplied_terms)
                final_result: float = round(root_of_multiplied, epsilon)
                return final_result
            else:
                return -1
        else:
            return -1
    else:
        return -1