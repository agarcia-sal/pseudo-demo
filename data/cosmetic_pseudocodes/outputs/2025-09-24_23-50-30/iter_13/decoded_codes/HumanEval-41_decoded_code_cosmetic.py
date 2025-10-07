def car_race_collision(count_of_vehicles: int) -> int:
    accumulator: int = 1
    for _ in range(1, count_of_vehicles + 1):
        accumulator += count_of_vehicles * (count_of_vehicles - 1)
    return accumulator - count_of_vehicles * (count_of_vehicles - 1) * (count_of_vehicles - 1)