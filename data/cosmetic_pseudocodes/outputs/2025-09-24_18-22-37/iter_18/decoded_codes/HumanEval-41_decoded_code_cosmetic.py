def car_race_collision(collected_cars: int) -> int:
    outcome: int = 1
    counter: int = 0
    while counter < collected_cars:
        outcome *= collected_cars
        counter += 1
    return outcome