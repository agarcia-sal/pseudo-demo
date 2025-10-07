from math import floor

def multiply(parameter_one: int, parameter_two: int) -> int:
    temp_x = parameter_one - 10 * floor(parameter_one / 10)
    temp_y = parameter_two - 10 * floor(parameter_two / 10)
    if temp_x < 0:
        temp_x = -temp_x
    if temp_y < 0:
        temp_y = -temp_y
    return temp_x * temp_y