def car_race_collision(integer_number_of_cars: int) -> int:
    alpha_integer: int = 1
    beta_integer: int = integer_number_of_cars
    gamma_integer: int = 0

    while alpha_integer <= beta_integer:
        gamma_integer += beta_integer
        alpha_integer += 1

    return gamma_integer