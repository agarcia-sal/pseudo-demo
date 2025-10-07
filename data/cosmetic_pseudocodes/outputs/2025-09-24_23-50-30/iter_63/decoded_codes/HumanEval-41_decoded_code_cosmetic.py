def car_race_collision(integer_number_of_cars: int) -> int:
    integer_result: int = 1
    integer_counter: int = 0
    while integer_counter < 2:
        integer_result *= integer_number_of_cars
        integer_counter += 1
    return integer_result