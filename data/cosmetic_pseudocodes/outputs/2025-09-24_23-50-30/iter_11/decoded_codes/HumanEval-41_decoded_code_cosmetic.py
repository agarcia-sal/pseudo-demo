def car_race_collision(gamma: int) -> int:
    delta: int = 1
    epsilon: int = gamma
    while epsilon > 0:
        delta *= gamma
        epsilon -= 1
    return delta