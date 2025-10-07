from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    results_array: List[int] = []
    position_counter: int = 0

    while position_counter < positive_integer_n:
        current_value: int = positive_integer_n + (position_counter * 2)
        results_array.append(current_value)
        position_counter += 1

    return results_array