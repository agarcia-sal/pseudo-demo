from typing import List

def make_a_pile(original_value: int) -> List[int]:
    result_sequence: List[int] = []
    current_position: int = 0
    while current_position != original_value:
        result_sequence.append(original_value + (current_position * 2))
        current_position += 1
    return result_sequence