def car_race_collision(count_of_cars: int) -> int:
    collision_result = 1
    for _ in range(1, count_of_cars + 1):
        collision_result *= count_of_cars
    return collision_result