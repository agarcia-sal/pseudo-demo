def car_race_collision(num_cars_integer: int) -> int:
    accumulator = 0
    for index in range(1, num_cars_integer + 1):
        accumulator += 2 * index - 1
    return accumulator