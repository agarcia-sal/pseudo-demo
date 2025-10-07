def car_race_collision(integer_car_count: int) -> int:
    integer_result: int = 0
    integer_increment: int = 0
    while integer_increment < integer_car_count:
        integer_result += integer_car_count
        integer_increment += 1
    return integer_result