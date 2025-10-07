def car_race_collision(cars_count: int) -> int:
    result = 1
    for _ in range(2):
        result *= cars_count
    return result