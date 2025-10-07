from typing import List


def tri(parameter_x: int) -> List[float]:
    if parameter_x == 0:
        return [1]
    else:
        variable_alpha: List[float] = [1, 3]
        variable_beta: int = 2
        while variable_beta <= parameter_x:
            if variable_beta % 2 == 0:
                variable_alpha.append(variable_beta / 2 + 1)
            else:
                temp_1: float = variable_alpha[variable_beta - 1]
                temp_2: float = variable_alpha[variable_beta - 2]
                temp_3: float = (variable_beta + 3) / 2
                variable_alpha.append(temp_1 + temp_2 + temp_3)
            variable_beta += 1
        return variable_alpha