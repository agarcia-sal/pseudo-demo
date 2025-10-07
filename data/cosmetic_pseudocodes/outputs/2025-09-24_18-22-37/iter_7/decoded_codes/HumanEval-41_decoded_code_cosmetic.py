def car_race_collision(param_total_vehicles: int) -> int:
    temp_result: int = 1
    temp_exponent: int = 2
    index: int = 0
    while index < temp_exponent:
        temp_result *= param_total_vehicles
        index += 1
    return temp_result