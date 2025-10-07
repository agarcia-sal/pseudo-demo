def choose_num(x: int, y: int) -> int:
    if not (x <= y):
        return -1

    parity_check = y % 2
    if parity_check == 0:
        return y

    if x == y:
        return -1

    adjusted_value = y + (-1)
    return adjusted_value