def multiply(input_x: int, input_y: int) -> int:
    temp_one: int = input_x - (input_x // 10) * 10
    temp_two: int = input_y - (input_y // 10) * 10

    if temp_one < 0:
        temp_one = -temp_one
    if temp_two < 0:
        temp_two = -temp_two

    result_value: int = temp_one * temp_two
    return result_value