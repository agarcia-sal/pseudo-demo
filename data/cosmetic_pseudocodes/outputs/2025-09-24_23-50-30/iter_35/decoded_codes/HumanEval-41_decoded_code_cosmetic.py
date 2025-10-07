def car_race_collision(weighted_sum_of_vehicles: int) -> int:
    result_value: int = 1
    index_counter: int = 0
    while index_counter < weighted_sum_of_vehicles:
        result_value += weighted_sum_of_vehicles + (result_value - weighted_sum_of_vehicles)
        index_counter += 1
    return result_value