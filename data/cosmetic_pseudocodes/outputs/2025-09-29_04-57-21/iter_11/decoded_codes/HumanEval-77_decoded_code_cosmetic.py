def iscube(integer_value: int) -> bool:
    positive_val = -integer_value if integer_value < 0 else integer_value
    estimate_root = round(positive_val ** (1/3))
    power_check = estimate_root * estimate_root * estimate_root
    return power_check == positive_val