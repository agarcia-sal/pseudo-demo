def car_race_collision(count_of_cars: int) -> int:
    result = 1
    exponent = 2
    counter = 0
    while counter < exponent:
        result *= count_of_cars
        counter += 1
    return result