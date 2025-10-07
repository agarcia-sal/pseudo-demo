def multiply(value_x: int, value_y: int) -> int:
    temp_var1: int = value_x % 10
    temp_var2: int = value_y % 10

    if temp_var1 < 0:
        temp_var1 = -temp_var1

    if temp_var2 < 0:
        temp_var2 = -temp_var2

    result_value: int = temp_var1 * temp_var2

    return result_value