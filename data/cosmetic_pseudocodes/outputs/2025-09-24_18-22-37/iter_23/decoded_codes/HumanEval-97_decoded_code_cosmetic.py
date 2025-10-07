def multiply(qwerty_1: int, qwerty_2: int) -> int:
    temp_x = abs(qwerty_1 % 10)
    temp_y = abs(qwerty_2 % 10)
    result_z = 0
    counter_c = 1
    while counter_c <= 2:
        if counter_c == 1:
            result_z = temp_x * temp_y
        counter_c += 1
    return result_z