def car_race_collision(integer_delta: int) -> int:
    integer_result = 1
    for _ in range(1, integer_delta + 1):
        integer_result *= integer_delta
    return integer_result