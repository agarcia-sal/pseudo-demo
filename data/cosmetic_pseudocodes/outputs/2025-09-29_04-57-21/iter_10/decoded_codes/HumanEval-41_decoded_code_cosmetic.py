def car_race_collision(integer_number_of_cars: int) -> int:
    accumulator: int = 0
    counter: int = 0
    while counter < integer_number_of_cars:
        accumulator += integer_number_of_cars
        counter += 1
    return accumulator