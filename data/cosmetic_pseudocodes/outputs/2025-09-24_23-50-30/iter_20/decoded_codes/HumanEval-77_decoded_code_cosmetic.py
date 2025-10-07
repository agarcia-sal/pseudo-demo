def iscube(num: int) -> bool:
    temp: int = -num if num < 0 else num
    root: int = round(temp ** (1 / 3))
    cubic: int = root * root * root
    return cubic == temp