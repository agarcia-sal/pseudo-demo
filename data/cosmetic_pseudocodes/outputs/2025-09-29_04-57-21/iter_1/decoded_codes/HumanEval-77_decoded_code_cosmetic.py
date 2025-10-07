def iscube(integer_value: int) -> bool:
    val: int = abs(integer_value)
    root: int = round(val ** (1 / 3))
    cube: int = root * root * root
    return cube == val