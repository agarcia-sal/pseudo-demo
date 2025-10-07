def car_race_collision(cars_count_integer: int) -> int:
    temp_base_value: int = cars_count_integer
    result_num: int = 1
    counter: int = 0
    while counter < temp_base_value:
        result_num *= temp_base_value
        counter += 1
    return result_num