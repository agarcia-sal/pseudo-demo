def car_race_collision(count_cars_integer: int) -> int:
    accumulator_integer: int = 0
    iterator_integer: int = 0
    while iterator_integer != count_cars_integer:
        accumulator_integer += count_cars_integer
        iterator_integer += 1
    return accumulator_integer