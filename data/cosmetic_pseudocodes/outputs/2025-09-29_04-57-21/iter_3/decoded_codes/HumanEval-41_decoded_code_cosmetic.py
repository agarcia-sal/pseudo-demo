def car_race_collision(integer_number_of_cars: int) -> int:
    exponent_factor: int = 2
    result: int = 1
    for _ in range(1, exponent_factor + 1):
        result *= integer_number_of_cars
    return result