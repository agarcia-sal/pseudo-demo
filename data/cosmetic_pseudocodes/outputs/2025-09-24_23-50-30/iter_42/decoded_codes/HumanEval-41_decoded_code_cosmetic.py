def car_race_collision(integer_input_cars: int) -> int:
    integer_index: int = 0
    integer_accumulator: int = 0
    while integer_index < integer_input_cars:
        integer_accumulator += integer_input_cars
        integer_index += 1
    return integer_accumulator