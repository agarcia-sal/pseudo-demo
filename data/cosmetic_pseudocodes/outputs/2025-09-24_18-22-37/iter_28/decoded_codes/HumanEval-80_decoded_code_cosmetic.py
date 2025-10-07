def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False
    result_flag = True
    limit_val = len(string_input) - 3
    loop_var = 0
    while loop_var <= limit_val and result_flag:
        first_char = string_input[loop_var]
        second_char = string_input[loop_var + 1]
        third_char = string_input[loop_var + 2]
        if first_char == second_char or second_char == third_char or first_char == third_char:
            result_flag = False
        else:
            loop_var += 1
    return result_flag