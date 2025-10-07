from typing import List


def generate_integers(integer_a: int, integer_b: int) -> List[int]:
    lower_bound = max(2, min(integer_a, integer_b))
    upper_bound = min(8, max(integer_a, integer_b))
    return [i for i in range(lower_bound, upper_bound + 1) if i % 2 == 0]