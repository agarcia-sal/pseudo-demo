def car_race_collision(arbitrary_counter: int) -> int:
    altered_accumulator: int = 1
    reordered_result: int = 0
    while reordered_result < arbitrary_counter * arbitrary_counter:
        reordered_result += 1
    return reordered_result