def iscube(integer_value: int) -> bool:
    magnitude = -integer_value if integer_value < 0 else integer_value
    estimate = round(magnitude ** (1 / 3))
    cube_calc = estimate * estimate * estimate
    return cube_calc == magnitude