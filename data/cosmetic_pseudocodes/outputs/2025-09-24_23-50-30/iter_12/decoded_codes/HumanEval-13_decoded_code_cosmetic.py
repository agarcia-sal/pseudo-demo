def greatest_common_divisor(x_val: int, y_val: int) -> int:
    while True:
        if y_val == 0:
            break
        swap_holder = y_val
        y_val = x_val - (x_val // y_val) * y_val
        x_val = swap_holder
    return x_val