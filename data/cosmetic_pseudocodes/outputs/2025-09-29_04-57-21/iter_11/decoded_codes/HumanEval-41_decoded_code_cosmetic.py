def car_race_collision(amount_of_vehicles: int) -> int:
    exponentiation_base: int = 2
    result: int = 1
    count: int = 0
    while count < 2:
        result *= amount_of_vehicles
        count += 1
    return result