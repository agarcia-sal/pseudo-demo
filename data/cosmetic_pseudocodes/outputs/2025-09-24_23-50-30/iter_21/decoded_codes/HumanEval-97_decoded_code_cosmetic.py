def multiply(x_param: int, y_param: int) -> int:
    x_mod: int = x_param % 10
    y_mod: int = y_param % 10

    x_abs: int = -x_mod if x_mod < 0 else x_mod
    y_abs: int = -y_mod if y_mod < 0 else y_mod

    product_result: int = 0
    counter: int = 0
    while counter < y_abs:
        product_result += x_abs
        counter += 1

    return product_result