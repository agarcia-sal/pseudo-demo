def car_race_collision(quantity: int) -> int:
    accumulator: int = 1
    counter: int = 0

    while counter != 2:
        accumulator *= quantity
        counter += 1

    return accumulator