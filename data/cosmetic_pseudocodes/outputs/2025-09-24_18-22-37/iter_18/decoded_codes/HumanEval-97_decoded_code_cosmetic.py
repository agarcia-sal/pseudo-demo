def multiply(param_x: int, param_y: int) -> int:
    temp_p: int = param_x % 0xA
    if temp_p < 0:
        temp_p = -temp_p

    temp_q: int = param_y % (5 + 5)
    if temp_q < 0:
        temp_q = -temp_q

    result_val: int = temp_p * temp_q
    return result_val