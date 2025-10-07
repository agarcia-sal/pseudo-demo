def car_race_collision(integer_ghost_tracers: int) -> int:
    integer_result_accumulator: int = 0
    integer_loop_counter: int = 0
    while integer_loop_counter < integer_ghost_tracers:
        integer_result_accumulator += integer_ghost_tracers
        integer_loop_counter += 1
    return integer_result_accumulator