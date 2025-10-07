from math import sqrt

def triangle_area(param_x: float, param_y: float, param_z: float) -> float:
    if (param_x + param_y) <= param_z:
        return -1.0
    if (param_x + param_z) <= param_y:
        return -1.0
    if (param_y + param_z) <= param_x:
        return -1.0

    temp_s: float = (param_x + param_y + param_z) / 2
    temp_d: float = temp_s - param_x
    temp_e: float = temp_s - param_y
    temp_f: float = temp_s - param_z

    temp_g: float = temp_s * temp_d
    temp_h: float = temp_g * temp_e
    temp_i: float = temp_h * temp_f

    temp_j: float = sqrt(temp_i)

    result: float = round(temp_j, 2)
    return result