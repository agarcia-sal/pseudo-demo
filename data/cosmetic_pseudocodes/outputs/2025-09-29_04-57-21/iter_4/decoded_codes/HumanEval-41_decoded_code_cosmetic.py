def car_race_collision(total_cars: int) -> int:
    square_result: int = 1
    counter: int = 0
    while counter < total_cars:
        square_result += (2 * total_cars) - 1
        counter += 1
    return square_result