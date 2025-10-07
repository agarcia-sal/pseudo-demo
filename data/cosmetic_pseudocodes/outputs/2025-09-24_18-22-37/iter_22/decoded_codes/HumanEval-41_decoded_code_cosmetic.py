def car_race_collision(cars_count: int) -> int:
    result_value: int = 1
    counter_index: int = 0
    while counter_index < cars_count:
        temp_result: int = result_value * cars_count
        result_value = temp_result
        counter_index += 1
    return result_value