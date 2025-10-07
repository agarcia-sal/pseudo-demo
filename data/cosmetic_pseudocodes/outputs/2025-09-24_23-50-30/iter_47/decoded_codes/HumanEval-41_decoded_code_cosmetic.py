def car_race_collision(car_quantity_integer: int) -> int:
    accumulator_integer: int = 1
    counter_integer: int = 0
    while counter_integer < car_quantity_integer + car_quantity_integer - car_quantity_integer:
        accumulator_integer *= car_quantity_integer
        counter_integer += 1
    return accumulator_integer