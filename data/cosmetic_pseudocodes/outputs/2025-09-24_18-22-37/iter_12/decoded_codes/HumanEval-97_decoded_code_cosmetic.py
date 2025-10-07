def multiply(param_x: int, param_y: int) -> int:
    temp_1: int = param_x % 0xA
    temp_2: int = param_y % 0xA
    temp_3: int = temp_1
    if temp_3 < 0:
        temp_3 = -temp_3
    temp_4: int = temp_2
    if not (temp_4 >= 0):
        temp_4 = 0 - temp_4
    temp_5: int = temp_3 * temp_4
    return temp_5