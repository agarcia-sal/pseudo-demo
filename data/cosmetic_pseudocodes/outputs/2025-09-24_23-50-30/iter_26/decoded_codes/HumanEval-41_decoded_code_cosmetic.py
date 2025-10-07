def car_race_collision(index_size_of_group: int) -> int:
    total_counter: int = 0
    pointer: int = 0
    while pointer != index_size_of_group:
        total_counter += index_size_of_group
        pointer += 1
    return total_counter