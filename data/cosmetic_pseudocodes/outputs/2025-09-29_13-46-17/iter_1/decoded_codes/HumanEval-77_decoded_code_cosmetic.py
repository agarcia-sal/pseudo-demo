def iscube(integer_value: int) -> bool:
    num = abs(integer_value)
    root = round(num ** (1 / 3))
    cube_check = root * root * root
    return cube_check == num