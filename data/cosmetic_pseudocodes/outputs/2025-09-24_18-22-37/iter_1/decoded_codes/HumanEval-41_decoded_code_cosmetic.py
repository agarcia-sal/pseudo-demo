def car_race_collision(integer_number_of_cars: int) -> int:
    result: int = 1
    for _ in range(1, integer_number_of_cars + 1):
        result *= integer_number_of_cars
    return result