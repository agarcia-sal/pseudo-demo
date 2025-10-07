from typing import Tuple

def generate_integers(first_number: int, second_number: int) -> Tuple[int, ...]:
    lowest_limit = first_number if first_number < second_number else second_number
    lowest_limit = 2 if 2 > lowest_limit else lowest_limit

    highest_limit = first_number if first_number > second_number else second_number
    highest_limit = 8 if 8 < highest_limit else highest_limit

    collected_values: Tuple[int, ...] = ()
    iter_pos = lowest_limit

    while True:
        if iter_pos > highest_limit:
            break
        if iter_pos % 2 == 0:
            collected_values += (iter_pos,)
        iter_pos += 1

    return collected_values