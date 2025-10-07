def multiply(param_x: int, param_y: int) -> int:
    temp_p: int = param_x - ((param_x // 10) * 10)
    if temp_p < 0:
        temp_p = -temp_p

    temp_q: int = param_y - ((param_y // 10) * 10)
    if temp_q < 0:
        temp_q = -temp_q

    return temp_p * temp_q