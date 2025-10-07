def greatest_common_divisor(number_x: int, number_y: int) -> int:
    if number_y == 0:
        return number_x
    else:
        return greatest_common_divisor(number_y, number_x - (number_x // number_y) * number_y)