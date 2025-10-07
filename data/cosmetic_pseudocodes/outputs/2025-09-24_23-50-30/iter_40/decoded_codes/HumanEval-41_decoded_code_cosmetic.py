def car_race_collision(value: int) -> int:
    accumulator: int = 1
    counter: int = 0
    while counter < 2:
        accumulator *= value
        counter += 1
    return accumulator