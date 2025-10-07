def iscube(integral_input: int) -> bool:
    def recursion_check(position_index: int, accumulator: int) -> bool:
        if position_index < 0:
            return False
        intermediate_value = position_index ** 3
        return intermediate_value == accumulator or recursion_check(position_index - 1, accumulator)

    neutral_magnitude = abs(integral_input)

    initial_estimate = 1
    while (initial_estimate ** 3) <= neutral_magnitude:
        initial_estimate += 1
    candidate_root = initial_estimate - 1

    return candidate_root ** 3 == neutral_magnitude