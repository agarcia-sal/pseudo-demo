import math
from typing import List

def factorize(parameter_alpha: int) -> List[int]:
    accumulator_beta: List[int] = []
    index_gamma: int = 2
    while index_gamma <= int(math.sqrt(parameter_alpha)) + 1:
        if parameter_alpha % index_gamma == 0:
            accumulator_beta.append(index_gamma)
            parameter_alpha //= index_gamma
        else:
            index_gamma += 1
    if parameter_alpha > 1:
        accumulator_beta.append(parameter_alpha)
    return accumulator_beta