def iscube(number: int) -> bool:
    magnitude = abs(number)
    estimated_root = round(magnitude ** (1 / 3))
    check_cube = estimated_root * estimated_root * estimated_root
    return check_cube == magnitude