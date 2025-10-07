def iscube(integer_value: int) -> bool:
    magnitude = -integer_value if integer_value < 0 else integer_value
    estimated_root = round(magnitude ** (1 / 3))
    cubed_estimate = estimated_root * estimated_root * estimated_root
    return cubed_estimate == magnitude