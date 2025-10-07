def car_race_collision(h_num: int) -> int:
    temp_base: int = h_num
    temp_exponent: int = 2
    temp_result: int = 1
    counter: int = 0

    while counter < temp_exponent:
        temp_result *= temp_base
        counter += 1

    return temp_result