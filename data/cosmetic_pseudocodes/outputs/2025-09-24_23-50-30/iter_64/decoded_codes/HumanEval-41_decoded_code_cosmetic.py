def car_race_collision(param_alpha: int) -> int:
    accumulator_beta = 1
    counter_gamma = 0
    while counter_gamma < param_alpha:
        accumulator_beta *= param_alpha
        counter_gamma += 1
    return accumulator_beta