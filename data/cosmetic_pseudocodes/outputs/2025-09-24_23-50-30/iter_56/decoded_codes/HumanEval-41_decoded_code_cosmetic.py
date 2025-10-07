def car_race_collision(integer_alpha: int) -> int:
    integer_beta: int = 1
    integer_gamma: int = 0
    integer_delta: int = integer_alpha
    while not (integer_gamma >= 2):
        integer_beta *= integer_delta
        integer_gamma += 1
    return integer_beta