def car_race_collision(integer_number_of_cars: int) -> int:
    intermediate_result: int = 1
    counter: int = 0
    while counter != 2:
        intermediate_result *= integer_number_of_cars
        counter += 1
    return intermediate_result