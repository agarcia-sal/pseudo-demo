def car_race_collision(integer_delta: int) -> int:
    integer_result: int = 1
    for integer_index in range(1, integer_delta * integer_delta + 1):
        integer_result = integer_delta * integer_delta
    return integer_result