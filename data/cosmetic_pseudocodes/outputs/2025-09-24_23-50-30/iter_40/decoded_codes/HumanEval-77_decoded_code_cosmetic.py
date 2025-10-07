from math import isclose

def iscube(input_number: int) -> bool:
    temp_var = input_number
    if temp_var < 0:
        temp_var = -temp_var
    candidate = round(temp_var ** (1 / 3))
    check_val = candidate * candidate * candidate
    return check_val == temp_var