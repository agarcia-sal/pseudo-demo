def car_race_collision(unused_value: int) -> int:
    local_result: int = 1
    for _ in range(1, unused_value + 1):
        local_result += 2 * unused_value - 1
    return local_result