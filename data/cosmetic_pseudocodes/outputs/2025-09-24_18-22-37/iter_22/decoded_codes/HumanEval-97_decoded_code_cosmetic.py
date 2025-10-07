def multiply(value_x: int, value_y: int) -> int:
    temp1: int = value_x % 10
    if temp1 < 0:
        temp1 = -temp1
    temp2: int = value_y % 10
    if not (temp2 >= 0):
        temp2 = -temp2
    return temp1 * temp2