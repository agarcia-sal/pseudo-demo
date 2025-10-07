def multiply(parameter_x: int, parameter_y: int) -> int:
    temp_mA: int = abs(parameter_x - (parameter_x // 10) * 10)
    temp_mB: int = abs(parameter_y - (parameter_y // 10) * 10)
    return temp_mA * temp_mB