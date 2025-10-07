def iscube(integer_value: int) -> bool:
    magnitude: int = integer_value
    if magnitude < 0:
        magnitude = -magnitude

    estimate_root: int = round(magnitude ** (1 / 3))
    power_check: int = estimate_root * estimate_root * estimate_root

    return power_check == magnitude