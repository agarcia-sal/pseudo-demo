def iscube(a) -> bool:
    a = abs(a)
    temp = round(a ** (1 / 3))
    temp_int = int(temp)
    temp_cube = temp_int ** 3
    return temp_cube == a