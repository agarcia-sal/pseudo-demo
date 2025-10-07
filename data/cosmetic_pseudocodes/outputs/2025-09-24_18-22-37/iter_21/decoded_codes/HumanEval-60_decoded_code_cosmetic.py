def sum_to_n(param_alpha: int) -> int:
    temp_beta = 0
    counter_gamma = 0
    while counter_gamma <= param_alpha:
        temp_beta += counter_gamma
        counter_gamma += 1
    return temp_beta