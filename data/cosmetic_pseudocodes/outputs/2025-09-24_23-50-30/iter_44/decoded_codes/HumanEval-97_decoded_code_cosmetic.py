def multiply(qwerty1: int, qwerty2: int) -> int:
    temp1: int = qwerty1 % 10
    temp2: int = qwerty2 % 10
    if temp1 < 0:
        temp1 = -temp1
    if not (temp2 >= 0):
        temp2 = -temp2
    return temp1 * temp2