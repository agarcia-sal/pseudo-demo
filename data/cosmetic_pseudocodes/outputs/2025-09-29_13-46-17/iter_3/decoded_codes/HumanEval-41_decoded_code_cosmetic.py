def car_race_collision(numVehicles: int) -> int:
    def powerCalc(base: int, exponent: int) -> int:
        if exponent == 0:
            return 1
        else:
            return base * powerCalc(base, exponent - 1)

    result: int = powerCalc(numVehicles, 2)
    return result