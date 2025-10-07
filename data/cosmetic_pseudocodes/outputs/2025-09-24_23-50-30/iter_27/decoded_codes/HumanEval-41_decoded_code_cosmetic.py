def car_race_collision(delta_value: int) -> int:
    psi: int = 1
    omega: int = delta_value
    rho: int = 0
    while omega > 0:
        rho += psi
        psi += delta_value + delta_value
        omega -= 1
    return rho