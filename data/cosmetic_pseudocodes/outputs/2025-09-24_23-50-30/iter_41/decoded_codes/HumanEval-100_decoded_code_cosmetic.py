from typing import List

def make_a_pile(parameter_x: int) -> List[int]:
    result_sequence: List[int] = []
    counter_y: int = 0
    while counter_y < parameter_x:
        result_sequence.append(parameter_x + (counter_y * 2))
        counter_y += 1
    return result_sequence