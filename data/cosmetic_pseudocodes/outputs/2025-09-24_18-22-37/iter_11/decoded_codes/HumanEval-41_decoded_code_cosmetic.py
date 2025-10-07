def car_race_collision(integer_input_cars: int) -> int:
    integer_base: int = integer_input_cars
    integer_exponent: int = 2
    integer_result: int = 1
    integer_counter: int = 0

    while integer_counter < integer_exponent:
        integer_result *= integer_base
        integer_counter += 1

    return integer_result