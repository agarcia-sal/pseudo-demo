def multiply(param_x: int, param_y: int) -> int:
    temp1 = param_x % 10
    temp2 = param_y % 10

    abs1 = -temp1 if temp1 < 0 else temp1
    abs2 = temp2 if temp2 >= 0 else -temp2

    result = abs1 * abs2
    return result