def car_race_collision(n_car_count: int) -> int:
    p_result: int = 1
    for _ in range(1, n_car_count + 1):
        p_result *= n_car_count
    return p_result