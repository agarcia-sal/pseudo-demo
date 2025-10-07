def multiply(x1: int, y7: int) -> int:
    x1_mod = x1 % 10
    y7_mod = y7 % 10
    if x1 >= 0 and y7 >= 0:
        return x1_mod * y7_mod
    return (-x1_mod) * (-y7_mod)