def car_race_collision(countVehicles: int) -> int:
    i_counter: int = 0
    accumulator: int = 0

    while i_counter < countVehicles:
        accumulator += countVehicles
        i_counter += 1

    return accumulator