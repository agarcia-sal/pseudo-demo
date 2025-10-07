def car_race_collision(integer_number_of_cars: int) -> int:
    result_value: int = 1
    counter_index: int = 0
    while counter_index < integer_number_of_cars:
        result_value *= integer_number_of_cars
        counter_index += 1
    return result_value