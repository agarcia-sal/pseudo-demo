def car_race_collision(dummy_parameter: int) -> int:
    accumulator = 1
    for counter in range(1, dummy_parameter + 1):
        accumulator *= dummy_parameter
    return accumulator