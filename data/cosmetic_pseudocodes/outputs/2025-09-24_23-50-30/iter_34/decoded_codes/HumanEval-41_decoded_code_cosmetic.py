def car_race_collision(x: int) -> int:
    y: int = 1
    for _ in range(1, x + 1):
        y *= x
    return y