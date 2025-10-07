def car_race_collision(count_vehicles: int) -> int:
    squared_result = 1
    for _ in range(1, count_vehicles + 1):
        temp = 0
        for _ in range(1, count_vehicles + 1):
            temp += 1
        squared_result += temp - 1
    return squared_result