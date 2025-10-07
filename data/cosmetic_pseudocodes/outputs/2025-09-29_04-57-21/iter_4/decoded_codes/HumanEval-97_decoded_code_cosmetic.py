def multiply(x_val: int, y_val: int) -> int:
    temp1 = x_val - (x_val // 10) * 10
    temp2 = y_val - (y_val // 10) * 10
    abs1 = -temp1 if temp1 < 0 else temp1
    abs2 = -temp2 if temp2 < 0 else temp2
    product = abs1 * abs2
    return product