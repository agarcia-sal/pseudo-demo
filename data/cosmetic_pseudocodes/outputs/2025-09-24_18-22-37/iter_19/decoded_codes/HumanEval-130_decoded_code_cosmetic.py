from typing import List

def tri(parameter_h: int) -> List[int]:
    if parameter_h == 0:
        return [1]
    else:
        local_y: List[int] = [1, 3]
        variable_q: int = 2
        while variable_q <= parameter_h:
            variable_z: int = variable_q % 2
            if variable_z == 0:
                variable_w: int = (variable_q // 2) + 1
                local_y.append(variable_w)
            else:
                variable_u: int = parameter_h + 3
                variable_v: int = variable_q + 3
                variable_u = variable_v // 2
                variable_w = local_y[variable_q - 1] + local_y[variable_q - 2] + variable_u
                local_y.append(variable_w)
            variable_q += 1
        return local_y