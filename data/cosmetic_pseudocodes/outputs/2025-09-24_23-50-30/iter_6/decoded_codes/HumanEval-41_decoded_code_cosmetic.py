def car_race_collision(integer_quantity_of_vehicles: int) -> int:
    accumulator: int = 0
    iterator: int = 0
    while iterator < integer_quantity_of_vehicles:
        accumulator += integer_quantity_of_vehicles
        iterator += 1
    return accumulator