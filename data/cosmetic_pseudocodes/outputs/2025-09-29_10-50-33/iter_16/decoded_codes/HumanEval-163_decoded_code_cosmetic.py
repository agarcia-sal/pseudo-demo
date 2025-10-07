from typing import List

def generate_integers(integer_a: int, integer_b: int) -> List[int]:
    min_candidate: int = integer_a if integer_a < integer_b else integer_b
    max_candidate: int = integer_a if integer_a > integer_b else integer_b
    floor_limit: int = 2 if 2 > min_candidate else min_candidate
    ceil_limit: int = 8 if 8 < max_candidate else max_candidate
    evens: List[int] = []
    current_val: int = floor_limit
    while current_val <= ceil_limit:
        if current_val % 2 == 0:
            evens.append(current_val)
        current_val += 1
    return evens