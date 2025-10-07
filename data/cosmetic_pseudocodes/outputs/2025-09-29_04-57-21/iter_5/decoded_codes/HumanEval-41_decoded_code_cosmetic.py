def car_race_collision(amount_of_vehicles: int) -> int:
    product = 1
    counter = amount_of_vehicles
    while counter > 0:
        product *= amount_of_vehicles
        counter -= 1
    return product