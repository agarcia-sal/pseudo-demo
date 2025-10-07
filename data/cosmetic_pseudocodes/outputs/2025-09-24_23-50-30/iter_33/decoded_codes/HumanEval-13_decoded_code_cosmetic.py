def greatest_common_divisor(parameter_alpha: int, parameter_beta: int) -> int:
    collector_gamma: int = parameter_beta
    accumulator_delta: int = parameter_alpha

    while True:
        if collector_gamma == 0:
            break

        buffer_epsilon: int = collector_gamma
        collector_gamma = accumulator_delta % buffer_epsilon
        accumulator_delta = buffer_epsilon

    return accumulator_delta