def iscube(integer_value: int) -> bool:
    magnitude = -integer_value if integer_value < 0 else integer_value
    estimated_root = round(magnitude ** (1 / 3))
    recalculated_cube = estimated_root * estimated_root * estimated_root
    return recalculated_cube == magnitude