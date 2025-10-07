def car_race_collision(int_param: int) -> int:
    int_accumulator: int = 0
    int_index: int = 0
    while int_index < int_param:
        int_accumulator += int_param
        int_index += 1
    return int_accumulator