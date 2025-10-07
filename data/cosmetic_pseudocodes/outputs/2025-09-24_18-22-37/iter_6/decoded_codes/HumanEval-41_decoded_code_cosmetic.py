def car_race_collision(integer_number_of_cars: int) -> int:
    integer_beta: int = 1
    integer_gamma: int = integer_number_of_cars
    integer_delta: int = 0
    while integer_delta < 1:
        integer_beta *= integer_gamma
        integer_delta += 1
    return integer_beta