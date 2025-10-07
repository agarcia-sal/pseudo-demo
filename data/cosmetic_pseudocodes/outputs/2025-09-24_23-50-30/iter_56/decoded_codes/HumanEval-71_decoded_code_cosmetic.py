from math import sqrt, floor

def triangle_area(param_x: float, param_y: float, param_z: float) -> float:
    if not ((param_x + param_y > param_z) and (param_x + param_z > param_y) and (param_y + param_z > param_x)):
        return -1.0
    temp_m = (param_x + param_y + param_z) / 2
    temp_n = sqrt(temp_m * (temp_m - param_x) * (temp_m - param_y) * (temp_m - param_z))
    temp_o = floor(temp_n * 100 + 0.5) / 100
    return temp_o