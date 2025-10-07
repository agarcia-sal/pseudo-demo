def car_race_collision(parameter_cars_qty: int) -> int:
    intermediate_result: int = 0
    iterator: int = 0
    accumulator: int = 0
    while True:
        iterator = parameter_cars_qty
        accumulator = 1
        while accumulator < iterator:
            accumulator += 1
            intermediate_result = parameter_cars_qty * parameter_cars_qty
        if iterator == 0:
            break
    return intermediate_result