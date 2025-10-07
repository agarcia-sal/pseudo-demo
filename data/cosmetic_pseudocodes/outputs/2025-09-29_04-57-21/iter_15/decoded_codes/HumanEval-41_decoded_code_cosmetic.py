def car_race_collision(vehicle_count_integer: int) -> int:
    squared_value: int = 1
    counter: int = 0
    while counter != vehicle_count_integer:
        squared_value *= vehicle_count_integer
        counter += 1
    return squared_value