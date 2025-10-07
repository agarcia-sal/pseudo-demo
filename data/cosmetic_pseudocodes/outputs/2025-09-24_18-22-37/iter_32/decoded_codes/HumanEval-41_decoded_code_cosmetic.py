def car_race_collision(parameter_vehicle_count: int) -> int:
    temporary_result: int = 1
    for counter_variable in range(1, parameter_vehicle_count + 1):
        temporary_result *= parameter_vehicle_count
    return temporary_result