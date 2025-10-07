def iscube(number_input: int) -> bool:
    positive_variant = -number_input if number_input < 0 else number_input
    estimate_root = round(positive_variant ** (1 / 3))
    check_cube = estimate_root * estimate_root * estimate_root
    return check_cube == positive_variant