def car_race_collision(amount_of_vehicles: int) -> int:
    exponentiation_base: int = amount_of_vehicles
    exponentiation_power: int = 1 + 1
    accumulation_result: int = 1

    while exponentiation_power > 0:
        accumulation_result *= exponentiation_base
        exponentiation_power -= 1

    return accumulation_result