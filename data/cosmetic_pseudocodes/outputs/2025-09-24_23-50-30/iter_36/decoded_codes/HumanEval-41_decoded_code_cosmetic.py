def car_race_collision(integer_alpha: int) -> int:
    integer_beta: int = 1
    integer_gamma: int = 0
    while integer_gamma < 2:
        integer_beta *= integer_alpha
        integer_gamma += 1
    return integer_beta