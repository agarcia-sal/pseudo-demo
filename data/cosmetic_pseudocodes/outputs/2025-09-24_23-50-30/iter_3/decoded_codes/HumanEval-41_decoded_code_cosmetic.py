def car_race_collision(n: int) -> int:
    result: int = 1
    for i in range(1, n + 1):
        result += (n + n - 1) * i - (i * i)
    return result