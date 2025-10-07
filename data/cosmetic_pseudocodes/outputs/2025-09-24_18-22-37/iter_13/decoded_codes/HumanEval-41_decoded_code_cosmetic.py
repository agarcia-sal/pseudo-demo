def car_race_collision(input_vehicle_count: int) -> int:
    temp_result: int = 2
    output_value: int = 1
    while temp_result > 0:
        output_value *= input_vehicle_count
        temp_result -= 1
    return output_value