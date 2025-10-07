def multiply(param_x: int, param_y: int) -> int:
    temp1: int = param_x % 10
    temp2: int = param_y % 10
    if temp1 < 0:
        temp1 = -temp1
    if temp2 < 0:
        temp2 = -temp2
    return temp1 * temp2