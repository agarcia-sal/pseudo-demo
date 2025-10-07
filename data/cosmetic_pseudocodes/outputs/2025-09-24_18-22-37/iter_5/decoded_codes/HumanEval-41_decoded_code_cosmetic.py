def car_race_collision(param_count_cars: int) -> int:
    temp_result: int = 1
    counter: int = 0
    while counter < 2:
        temp_result *= param_count_cars
        counter += 1
    return temp_result