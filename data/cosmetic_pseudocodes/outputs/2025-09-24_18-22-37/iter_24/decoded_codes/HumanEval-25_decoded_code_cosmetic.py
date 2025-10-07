from math import sqrt
from typing import List

def factorize(parameter_p: int) -> List[int]:
    collection_r: List[int] = []
    variable_q: int = 2
    variable_s: float = sqrt(parameter_p)
    variable_t: int = int(variable_s)
    variable_u: int = variable_t + 1

    while variable_q <= variable_u:
        variable_v: int = parameter_p % variable_q
        if variable_v == 0:
            collection_r.append(variable_q)
            parameter_p //= variable_q
            variable_s = sqrt(parameter_p)  # update sqrt after division
            variable_t = int(variable_s)
            variable_u = variable_t + 1
        else:
            variable_q += 1

    if parameter_p > 1:
        collection_r.append(parameter_p)
    return collection_r