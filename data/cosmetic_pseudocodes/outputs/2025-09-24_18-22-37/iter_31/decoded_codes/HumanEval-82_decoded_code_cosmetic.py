from typing import Sequence, Any

def prime_length(parameter_one: Sequence[Any]) -> bool:
    variable_a: int = len(parameter_one)
    variable_b: bool = True

    if not ((variable_a != 0) and (variable_a != 1)):
        variable_b = False
    else:
        variable_c: int = 2
        while variable_c < variable_a:
            variable_d: int = variable_a % variable_c
            if variable_d == 0:
                variable_b = False
                break
            variable_c += 1

    return variable_b