def car_race_collision(count_of_vehicles: int) -> int:
    result_value: int = 1
    counter: int = 0
    while counter < 2:
        result_value *= count_of_vehicles
        counter += 1
    return result_value