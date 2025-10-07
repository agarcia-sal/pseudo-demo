def iscube(integer_value: int) -> bool:
    temp_val: int = integer_value if integer_value >= 0 else -integer_value
    approx_root: int = round(temp_val ** (1 / 3))
    cube_check: int = approx_root * approx_root * approx_root
    return cube_check == temp_val