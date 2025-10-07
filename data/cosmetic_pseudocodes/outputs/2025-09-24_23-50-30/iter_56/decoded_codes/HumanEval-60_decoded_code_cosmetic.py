def sum_to_n(index_x: int) -> int:
    accumulator_y: int = 0
    counter_z: int = 0
    while counter_z <= index_x:
        accumulator_y += counter_z
        counter_z += 1
    return accumulator_y