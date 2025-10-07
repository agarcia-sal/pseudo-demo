def multiply(integer_a: int, integer_b: int) -> int:
    temp_x: int = integer_a % 10
    temp_y: int = integer_b % 10

    if temp_x < 0:
        temp_x = -temp_x

    if temp_y < 0:
        temp_y = -temp_y

    return temp_x * temp_y