def multiply(value_x: int, value_y: int) -> int:
    temp_one: int = value_x % 10
    if temp_one < 0:
        temp_one = -temp_one

    temp_two: int = value_y % 10
    if temp_two < 0:
        temp_two = -temp_two

    return temp_one * temp_two