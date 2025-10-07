from typing import List

def generate_integers(integer_a: int, integer_b: int) -> List[int]:
    start_value: int = integer_a if integer_a < integer_b else integer_b
    minimal_limit: int = 2
    if start_value < minimal_limit:
        start_value = minimal_limit

    end_value: int = integer_a if integer_a > integer_b else integer_b
    maximal_limit: int = 8
    if end_value > maximal_limit:
        end_value = maximal_limit

    result_collection: List[int] = [candidate_value for candidate_value in range(start_value, end_value + 1) if candidate_value % 2 == 0]

    return result_collection