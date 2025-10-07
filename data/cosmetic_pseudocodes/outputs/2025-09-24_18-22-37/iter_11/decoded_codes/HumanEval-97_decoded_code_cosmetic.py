def multiply(parameter_x: int, parameter_y: int) -> int:
    temp_p: int = parameter_x % 10
    if temp_p < 0:
        temp_p = -temp_p

    temp_q: int = parameter_y % 10
    if temp_q < 0:
        temp_q = -temp_q

    result_v: int = temp_p * temp_q
    return result_v