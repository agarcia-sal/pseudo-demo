def multiply(parameter_one: int, parameter_two: int) -> int:
    temp_var_1: int = parameter_one % 10
    temp_var_2: int = parameter_two % 10
    temp_var_3: int = temp_var_1
    if temp_var_3 < 0:
        temp_var_3 = -temp_var_3
    temp_var_4: int = temp_var_2
    if not (temp_var_4 >= 0):
        temp_var_4 = -temp_var_4
    combined_result: int = temp_var_3
    combined_result *= temp_var_4
    return combined_result