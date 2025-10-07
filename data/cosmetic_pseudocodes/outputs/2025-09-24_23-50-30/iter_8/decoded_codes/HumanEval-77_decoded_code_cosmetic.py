def iscube(integer_value: int) -> bool:
    value_abs: int = integer_value if integer_value >= 0 else -integer_value
    root_estimate: int = 0
    for candidate in range(value_abs + 2):  # +2 because range is exclusive upper bound
        if candidate ** 3 - value_abs >= 0:
            root_estimate = candidate
            break
    cube_check: int = root_estimate ** 3
    return cube_check == value_abs