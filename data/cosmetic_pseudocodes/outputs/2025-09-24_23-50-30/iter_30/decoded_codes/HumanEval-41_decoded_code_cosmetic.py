def car_race_collision(count_cars_integer: int) -> int:
    output_result_integer: int = 1
    counter_integer: int = 0
    while counter_integer != count_cars_integer:
        # The fraction simplifies to count_cars_integer since (count_cars_integer - 1)/(count_cars_integer - 1) == 1 if count_cars_integer != 1
        # But as per pseudocode, keep the expression faithful.
        output_result_integer += count_cars_integer * (count_cars_integer - 1) // (count_cars_integer - 1)  # integer division since output_result_integer is int
        counter_integer += 1
    return output_result_integer