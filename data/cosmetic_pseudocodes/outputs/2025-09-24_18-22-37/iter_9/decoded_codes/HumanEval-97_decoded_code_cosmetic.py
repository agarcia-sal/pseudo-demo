def multiply(delta_x: int, gamma_y: int) -> int:
    temp1: int = delta_x % 10
    temp2: int = gamma_y % 10
    abs_temp1: int = abs(temp1)
    abs_temp2: int = abs(temp2)
    result: int = abs_temp1 * abs_temp2
    return result