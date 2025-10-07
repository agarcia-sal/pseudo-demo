def car_race_collision(n: int) -> int:
    acc: int = 0
    i: int = 0
    while i < n * n:
        acc += 1
        i += 1
    return acc