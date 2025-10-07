def car_race_collision(amount_of_vehicles_integer: int) -> int:
    exponent_base: int = amount_of_vehicles_integer
    exponent_power: int = 2
    result_value: int = 1
    while exponent_power > 0:
        result_value *= exponent_base
        exponent_power -= 1
    return result_value