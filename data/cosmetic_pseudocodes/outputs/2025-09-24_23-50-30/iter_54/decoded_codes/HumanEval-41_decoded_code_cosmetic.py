def car_race_collision(count: int) -> int:
    accumulator: int = 1
    result: int = 1
    while accumulator <= count:
        result *= count
        accumulator += 1
    return result