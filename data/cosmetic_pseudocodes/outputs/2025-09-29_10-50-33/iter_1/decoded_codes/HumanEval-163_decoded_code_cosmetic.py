from typing import List

def generate_integers(integer_a: int, integer_b: int) -> List[int]:
    start_point: int = integer_a if integer_a < integer_b else integer_b
    end_point: int = integer_a if integer_a > integer_b else integer_b

    if start_point < 2:
        start_point = 2
    if end_point > 8:
        end_point = 8

    return [current_value for current_value in range(start_point, end_point + 1) if current_value % 2 == 0]