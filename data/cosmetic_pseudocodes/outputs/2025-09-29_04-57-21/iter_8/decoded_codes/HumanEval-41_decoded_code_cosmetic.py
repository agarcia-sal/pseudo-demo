def car_race_collision(total_vehicles: int) -> int:
    result_value: int = 1
    counter_val: int = 0
    while counter_val < 2:
        temp: int = result_value * total_vehicles
        result_value = temp
        counter_val += 1
    return result_value