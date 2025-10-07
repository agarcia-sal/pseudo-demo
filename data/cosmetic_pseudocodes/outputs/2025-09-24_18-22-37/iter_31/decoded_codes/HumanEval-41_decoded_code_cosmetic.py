def car_race_collision(integer_quantity_cars: int) -> int:
    result_value: int = 1
    counter: int = 0
    while counter < 2:
        result_value *= integer_quantity_cars
        counter += 1
    return result_value