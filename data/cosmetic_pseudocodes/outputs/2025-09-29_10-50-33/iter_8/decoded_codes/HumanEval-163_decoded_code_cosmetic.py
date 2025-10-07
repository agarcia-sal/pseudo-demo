from typing import List

def generate_integers(first_limit: int, second_limit: int) -> List[int]:
    def construct_list(current_value: int, max_value: int, accumulator: List[int]) -> List[int]:
        if current_value > max_value:
            return accumulator
        if current_value % 2 == 0:
            return construct_list(current_value + 1, max_value, accumulator + [current_value])
        return construct_list(current_value + 1, max_value, accumulator)

    low_marker = 2 if 2 > (first_limit if first_limit < second_limit else second_limit) else (first_limit if first_limit < second_limit else second_limit)
    high_marker = 8 if 8 < (first_limit if first_limit > second_limit else second_limit) else (first_limit if first_limit > second_limit else second_limit)

    return construct_list(low_marker, high_marker, [])