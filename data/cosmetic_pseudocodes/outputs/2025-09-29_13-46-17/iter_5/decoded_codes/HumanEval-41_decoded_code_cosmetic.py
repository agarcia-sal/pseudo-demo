def car_race_collision(tot_vehicle_count: int) -> int:
    acc: int = 0
    iCounter: int = 0
    while iCounter < tot_vehicle_count:
        jIndex: int = 0
        while jIndex < tot_vehicle_count:
            acc += 1
            jIndex += 1
        iCounter += 1
    return acc