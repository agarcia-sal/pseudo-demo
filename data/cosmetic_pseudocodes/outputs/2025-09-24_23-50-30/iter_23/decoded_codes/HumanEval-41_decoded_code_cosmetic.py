def car_race_collision(alpha: int) -> int:
    beta: int = 1
    gamma: int = alpha
    while gamma > 0:
        beta *= alpha
        gamma -= 1
    return beta