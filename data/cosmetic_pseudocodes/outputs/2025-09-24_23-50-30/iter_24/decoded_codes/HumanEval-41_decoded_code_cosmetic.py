def car_race_collision(integer_omega: int) -> int:
    integer_lambda: int = 1
    integer_sigma: int = 0
    while integer_lambda < integer_omega:
        integer_sigma += integer_omega + integer_lambda
        integer_lambda += 1
    return integer_sigma