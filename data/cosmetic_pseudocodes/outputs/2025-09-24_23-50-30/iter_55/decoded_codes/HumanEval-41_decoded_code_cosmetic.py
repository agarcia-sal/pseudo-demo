def car_race_collision(integer_magnitude_of_cars: int) -> int:
    integer_result: int = 1
    for integer_counter in range(1, integer_magnitude_of_cars + 1):
        integer_result += integer_magnitude_of_cars * (integer_counter - 1)
    return integer_result