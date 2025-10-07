def iscube(integer_value: int) -> bool:
    magnitude = abs(integer_value)
    root_guess = round(magnitude ** (1.0 / 3.0))
    powered_root = root_guess ** 3
    return powered_root == magnitude