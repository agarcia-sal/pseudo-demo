def iscube(integer_value: int) -> bool:
    abs_val = -integer_value if integer_value < 0 else integer_value
    root_approx = round(abs_val ** (1 / 3))
    cube_check = root_approx * root_approx * root_approx
    return cube_check == abs_val